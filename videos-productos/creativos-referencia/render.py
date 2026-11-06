from PIL import Image,ImageDraw,ImageFont
import math,subprocess,numpy as np,wave
from pathlib import Path
O=Path(__file__).resolve().parent;W,H,FPS,DUR=720,1280,24,32
INK='#171717';PAPER='#F7F6F2';BLUE='#3968DA';SKY='#CFDFEA';SAND='#D7C7AC';GOLD='#F3CA4C'
REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD=REG.replace('.ttf','-Bold.ttf');fonts={}
def font(n,b=True):
 k=(int(n),b)
 if k not in fonts:fonts[k]=ImageFont.truetype(BOLD if b else REG,int(n))
 return fonts[k]
def ease(x):x=max(0,min(1,x));return 1-(1-x)**3
def text(im,s,y,size=45,fill=INK,align='left',x=45):
 d=ImageDraw.Draw(im)
 for row in s.split('\n'):
  f=font(size);bb=d.textbbox((0,0),row,font=f);xx=(W-(bb[2]-bb[0]))/2 if align=='center' else x
  d.text((xx,y),row,font=f,fill=fill);y+=int(size*1.23)
def pill(im,s,x,y,dark=False):
 d=ImageDraw.Draw(im);f=font(18);bb=d.textbbox((0,0),s,font=f);ww=bb[2]+28
 d.rounded_rectangle((x,y,x+ww,y+36),18,fill=INK if dark else PAPER,outline=INK,width=2);d.text((x+14,y+7),s,font=f,fill=PAPER if dark else INK)
def star(d,x,y,r=14,color=GOLD):
 pts=[]
 for i in range(10):
  a=-math.pi/2+i*math.pi/5;rr=r if i%2==0 else r*.45;pts.append((x+math.cos(a)*rr,y+math.sin(a)*rr))
 d.polygon(pts,fill=color,outline=INK)
def person(im,x,y,s=1,role='customer',wave=0,walk=0):
 d=ImageDraw.Draw(im);skin='#EDBE99';shirt='#B4D1BE' if role=='customer' else '#FFFFFF';lw=max(2,int(3*s))
 # Coordinate is top center of head.
 def box(a):return tuple((x+v*s if i%2==0 else y+v*s) for i,v in enumerate(a))
 d.line(box((-18,137,-22+walk*9,235)),fill=INK,width=int(14*s));d.line(box((18,137,22-walk*9,235)),fill=INK,width=int(14*s))
 d.ellipse(box((-37,-2,37,72)),fill=skin,outline=INK,width=lw);d.pieslice(box((-38,-7,38,54)),180,360,fill='#392D25')
 for xx in [-13,13]:d.ellipse(box((xx-3,29,xx+3,36)),fill=INK)
 d.arc(box((-13,35,15,55)),5,170,fill=INK,width=lw)
 d.rounded_rectangle(box((-40,72,40,155)),int(10*s),fill=shirt,outline=INK,width=lw)
 if role=='waiter':d.rectangle(box((-29,103,29,153)),fill=INK);d.line(box((-22,75,-22,111)),fill=INK,width=lw);d.line(box((22,75,22,111)),fill=INK,width=lw)
 d.line(box((-37,84,-65,130)),fill=INK,width=int(10*s));d.line(box((37,84,75,100-60*wave)),fill=INK,width=int(10*s));d.ellipse(box((67,92-60*wave,85,110-60*wave)),fill=skin,outline=INK,width=lw)
 d.ellipse(box((-74,124,-58,141)),fill=skin,outline=INK,width=lw)
def mascot(im,cx,cy,w=260,kind='sticker',a=0,eyes=True):
 h=int(w*(1.35 if kind=='card' else 1));layer=Image.new('RGBA',(w+20,h+20));d=ImageDraw.Draw(layer);x=y=10;r=int(w*.1)
 d.rounded_rectangle((x,y,x+w,y+h),r,fill=PAPER,outline=INK,width=3)
 d.rounded_rectangle((x+3,y+3,x+w-3,y+h*.43),r-2,fill=BLUE)
 # Cover bottom blue corners for a straight dividing line.
 d.rectangle((x+3,y+h*.3,x+w-3,y+h*.43),fill=BLUE)
 for i in range(5):star(d,x+w*.28+i*w*.11,y+h*.11,w*.036)
 f=font(max(10,int(w*.062)));label='Dejá tu reseña';bb=d.textbbox((0,0),label,font=f);d.text((x+(w-bb[2])/2,y+h*.2),label,font=f,fill='white')
 if eyes:
  for ex in [x+w*.4,x+w*.6]:
   d.ellipse((ex-w*.045,y+h*.34,ex+w*.045,y+h*.34+w*.095),fill='white',outline=INK,width=2);d.ellipse((ex-w*.012,y+h*.35,ex+w*.022,y+h*.35+w*.048),fill=INK)
  d.arc((x+w*.40,y+h*.40,x+w*.63,y+h*.53),5,170,fill=INK,width=3)
 # Stylized NFC icon.
 for n in range(3):
  rr=w*(.065+n*.035);d.arc((x+w*.22-rr,y+h*.73-rr,x+w*.22+rr,y+h*.73+rr),-65,65,fill=INK,width=max(2,int(w*.012)))
 # Decorative matrix; intentionally not an actual QR.
 qx=int(x+w*.56);qy=int(y+h*.57);cell=max(2,int(w*.024));q=cell*13
 d.rectangle((qx-4,qy-4,qx+q+4,qy+q+4),fill='white',outline=INK,width=2)
 for row in range(13):
  for col in range(13):
   finder=None
   for fx,fy in [(0,0),(8,0),(0,8)]:
    if fx<=col<fx+5 and fy<=row<fy+5:
     dx=col-fx;dy=row-fy;finder=dx in [0,4] or dy in [0,4] or (dx==2 and dy==2);break
   on=finder if finder is not None else (row*7+col*3+row*col)%5<2
   if on:d.rectangle((qx+col*cell,qy+row*cell,qx+(col+1)*cell-1,qy+(row+1)*cell-1),fill=INK)
 layer=layer.rotate(a,Image.Resampling.BICUBIC,expand=True);im.paste(layer,(int(cx-layer.width/2),int(cy-layer.height/2)),layer)
def phone(im,x,y,w=200,mode='notification',phase=0):
 d=ImageDraw.Draw(im);h=w*1.8
 d.rounded_rectangle((x,y,x+w,y+h),25,fill=INK);d.rounded_rectangle((x+7,y+10,x+w-7,y+h-10),19,fill='white');d.rounded_rectangle((x+w*.32,y+15,x+w*.68,y+25),5,fill=INK)
 f=font(int(w*.071))
 if mode=='notification':
  d.rounded_rectangle((x+17,y+65,x+w-17,y+145),12,fill=SKY);d.text((x+25,y+78),'NFC detectado',font=f,fill=INK);d.text((x+25,y+109),'Abrir enlace',font=f,fill=BLUE)
 elif mode=='scan':
  d.rounded_rectangle((x+28,y+75,x+w-28,y+220),10,outline=INK,width=3);sy=y+80+phase*130;d.line((x+31,sy,x+w-31,sy),fill=BLUE,width=4);d.text((x+35,y+245),'Escaneá el QR',font=f,fill=INK)
 else:
  d.text((x+24,y+65),'Tu experiencia',font=f,fill=INK)
  d.rounded_rectangle((x+20,y+105,x+w-20,y+230),8,outline=INK,width=2)
  for n in range(3):d.line((x+30,y+126+n*25,x+w-40,y+126+n*25),fill='#B9C4CF',width=3)
  d.rounded_rectangle((x+25,y+257,x+w-25,y+295),9,fill=BLUE);d.text((x+46,y+268),'Publicar',font=f,fill='white')
def dashboard(im,u):
 d=ImageDraw.Draw(im);d.rounded_rectangle((65,470,655,825),22,fill='white',outline=INK,width=3)
 d.text((90,500),'Metricfield Reviews',font=font(28),fill=INK)
 for n,(title,num) in enumerate([('Usos','148'),('Reseñas','23')]):
  xx=90+n*275;d.rounded_rectangle((xx,565,xx+250,700),12,fill=SKY);d.text((xx+18,582),title,font=font(21),fill=INK);d.text((xx+18,620),str(int(int(num)*ease(u))),font=font(44),fill=INK)
 d.text((90,744),'Vista y datos ilustrativos',font=font(18,False),fill='#626262')
def base(bg,t,tag):
 im=Image.new('RGB',(W,H),bg);d=ImageDraw.Draw(im);d.text((45,42),'METRICFIELD  /  NFC + QR',font=font(16),fill=INK if bg!=INK else PAPER);pill(im,tag,45,1124,dark=bg!=INK)
 d.line((45,1225,675,1225),fill='#999999',width=2);d.line((45,1225,45+630*t/DUR,1225),fill=BLUE,width=5)
 return im

def draw(t,kind):
 st=kind=='sticker';cuts=[0,4,8,13,18,23,28,32];idx=min(6,next((n for n in range(7) if t<cuts[n+1]),6));u=t-cuts[idx];bg=[PAPER,INK,SAND,SKY,PAPER,SKY,PAPER][idx];im=base(bg,t,'STICKER NFC + QR' if st else 'TARJETA NFC + QR');d=ImageDraw.Draw(im)
 if idx==0:
  text(im,'Tu cliente se fue\nfeliz…' if st else 'Buen café.\nBuena atención.',135,47)
  # Counter and characters, customer leaving to right.
  person(im,185,540,1.25,'waiter',wave=.5+.3*math.sin(u*3));d.rectangle((55,734,315,960),fill=SAND,outline=INK,width=3);d.rectangle((40,726,330,747),fill='white',outline=INK,width=3)
  xx=435+65*ease(u/3);person(im,xx,570,1.35,'customer',wave=.5,walk=math.sin(u*8))
  text(im,'¿Y la reseña?' if st else 'La cuenta llegó.\n¿La reseña también?',965,43)
  if u>1.3:pill(im,'Pendiente…',385,435)
 elif idx==1:
  text(im,'Tu mostrador tiene\nun superpoder.' if st else 'La tarjeta que pide\nla palabra.',140,44,PAPER)
  # Orbiting mascot with personality and particle stars.
  for n in range(3):
   r=140+n*45;d.ellipse((360-r,660-r,360+r,660+r),outline='#494949',width=2)
  mascot(im,360,650+12*math.sin(u*3),300,kind,a=7*math.sin(u*2))
  for n in range(4):star(d,360+230*math.cos(u+n*1.57),660+230*math.sin(u+n*1.57),14)
  text(im,'No vuela.\nTe acerca a la opinión.' if st else 'Chiquita en la mano.\nGrande en el momento.',972,32,PAPER)
 elif idx==2:
  text(im,'Pegalo donde\ntermina la visita.' if st else 'El último paso\ndel buen servicio.',135,45)
  if st:
   d.polygon([(0,790),(720,690),(720,1020),(0,1120)],fill='#B89972',outline=INK);mascot(im,360,710+90*(1-ease(u/1.2)),270,kind,a=-8+6*math.sin(u))
   pill(im,['CAJA','MESA','MOSTRADOR'][min(2,int(u/1.67))],260,1000)
   if u<1.8:
    d.line((500,510,435,600+70*ease(u)),fill=INK,width=22);d.ellipse((420,587+70*ease(u),450,617+70*ease(u)),fill='#EDBE99',outline=INK,width=2)
  else:
   person(im,200,500,1.8,'waiter',wave=.5);mascot(im,460,670,195,kind,a=8*math.sin(u));pill(im,'JUNTO CON LA CUENTA',190,1000)
 elif idx==3:
  text(im,'Un toque.\nO un escaneo.',135,50)
  mascot(im,215,710,240,kind,a=-5)
  px=480-100*ease(u/1.3);phone(im,px,490,215,'notification' if u<2.5 else 'scan',phase=(u*.7)%1)
  for n in range(3):
   r=20+((u*.65+n*.3)%1)*80;d.arc((300-r,700-r,300+r,700+r),-65,65,fill=BLUE,width=3)
  text(im,'NFC: acercá y tocá el aviso.' if u<2.5 else 'QR: abrí la cámara y escaneá.',982,28)
  text(im,'NFC requiere un celular compatible.',1040,18)
 elif idx==4:
  text(im,'Menos vueltas.\nMás fácil opinar.',135,46)
  phone(im,250,440,220,'review');person(im,585,740,1.0,'customer',wave=.8+.15*math.sin(u*2))
  # Traveling path dots from product to screen.
  mascot(im,125,735,135,kind,a=4*math.sin(u))
  for n in range(5):d.ellipse((205+n*11,720+8*math.sin(u*4+n),210+n*11,725+8*math.sin(u*4+n)),fill=BLUE)
  text(im,'El cliente escribe\ny publica su opinión.',975,33)
 elif idx==5:
  text(im,'El producto acerca.\nEl software acompaña.',135,39)
  dashboard(im,u/1.4)
  mascot(im,580,920,110,kind,a=10*math.sin(u*2));text(im,'Conocé\nMetricfield Reviews.',950,33)
 else:
  text(im,'Tu mostrador,\ncon otra misión.' if st else 'La cuenta se cierra.\nLa experiencia\nse comparte.',135,43)
  mascot(im,360,700+13*math.sin(u*3),300,kind,a=6*math.sin(u*2))
  for n in range(3):star(d,180+n*180,470+15*math.sin(u*3+n),14)
  text(im,'Hacé fácil pedir\nuna reseña en Google.',1000,33)
 # Tiny editorial note, never use decorative QR as a working demo.
 d=ImageDraw.Draw(im);d.text((45,1180),'Animación ilustrativa · Opiniones reales de tus clientes',font=font(14,False),fill='#777777' if bg!=INK else '#BBBBBB')
 dist=min(abs(t-b) for b in cuts);fade=min(1,dist/.11)
 if fade<1:im=Image.blend(Image.new('RGB',(W,H),bg),im,fade)
 return im

def music(kind):
 sr=44100;n=sr*DUR;a=np.zeros(n,dtype=np.float32);rng=np.random.default_rng(49 if kind=='sticker' else 71);step=.4 if kind=='sticker' else .428571
 for k,b in enumerate(np.arange(0,DUR,step)):
  i=int(b*sr);ln=min(int(.35*sr),n-i);x=np.arange(ln)/sr
  if k%2==0:a[i:i+ln]+=.1*np.sin(2*np.pi*(55*x+.7*(1-np.exp(-x*40))))*np.exp(-x*15)
  ll=min(int(.04*sr),n-i);xx=np.arange(ll)/sr;a[i:i+ll]+=.012*rng.normal(size=ll)*np.exp(-xx*100)
  freq=([392,493.88,587.33,739.99] if kind=='sticker' else [329.63,392,493.88,659.25])[k%4]
  a[i:i+ln]+=.045*np.sin(2*np.pi*freq*x)*np.exp(-x*13)
 # Comic sparkle sounds at scene changes.
 for b in [4,8,13,18,23,28]:
  i=int(b*sr);ln=min(int(.3*sr),n-i);x=np.arange(ln)/sr;a[i:i+ln]+=.055*np.sin(2*np.pi*(650*x+1100*x*x))*np.exp(-x*18)
 a*=np.minimum(1,np.arange(n)/sr)*np.minimum(1,(n-np.arange(n))/sr)
 path=O/f'{kind}-musica.wav'
 with wave.open(str(path),'wb') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(sr);f.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
 return path

for kind in ['sticker','card']:
 name='01-sticker-superpoder' if kind=='sticker' else '02-tarjeta-buen-servicio';audio=music(kind)
 proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pixel_format','rgb24','-video_size','720x1280','-framerate',str(FPS),'-i','-','-i',str(audio),'-vf','scale=1080:1920:flags=lanczos','-c:v','libx264','-preset','fast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart','-threads','2',str(O/(name+'.mp4'))],stdin=subprocess.PIPE)
 for i in range(FPS*DUR):
  proc.stdin.write(draw(i/FPS,kind).tobytes())
  if i%(FPS*8)==0:print(name,i//FPS,'/',DUR,flush=True)
 proc.stdin.close();assert proc.wait()==0
 for t in [2,6,10,15,20,25,30]:draw(t,kind).save(O/f'{name}-{t}.jpg')
 print('CREATED',name,flush=True)

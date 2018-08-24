#!/usr/bin/python
'''
   33  python -c "a='./.cache/mozilla/firefox/fvve1u9s.default/cache2/entries/';import os;print[a+x[:-1] for x in os.popen('ls -rt '+a+' |tail -10')] "
   35  python -c "a='./.cache/mozilla/firefox/fvve1u9s.default/cache2/entries/';import os;print[x[:-1] for x in os.popen('find '+a+' -mtime -1 |tail -10')] "
url=  'https://vk.com/massass?z=photo'
'''
import pyautogui
import os,re,time
url=  'https://vk.com/massass?z=photo'
print url
#os.system('/usr/bin/opera '+url)
a='/home/val/.cache/mozilla/firefox/fvve1u9s.default/cache2/entries/'
print a
k=-1
while (1) :
        k=k+1
        if k%2 == 0: cmd='find '+a+' -mtime -1 |tail -10'
        if k%2 != 0: cmd=        'ls -rt '+a+' |tail -10'
        print cmd
#       pyautogui.moveTo(650, 350) # Right arrow ->
        pyautogui.click()
        print pyautogui.position()
        time.sleep(2)
#       9  
        print 'ls *.jpg|wc'
        os.system('ls /home/val/test_pix/*.jpg|wc')
        if k%2==0: lst=[  x for x in os.popen( cmd )]
        if k%2!=0: lst=[a+x for x in os.popen( cmd )]
        print 'len(lst)=',len(lst)
        print 'lst: ',lst[:3]
        lst1=[]
        for x in lst:
          lst1=lst1+ [y.split()[-1] for y in os.popen('xxd '+x[:-1])]
        print 'len(lst1)=',len(lst1)
        xxx=''
        for x in lst1:
          xxx=xxx+x
        print 'xxx=',xxx[0:100]
        print 'len(xxx)=',len(xxx)
        lst2=xxx.split('//pp')
        print 'len(lst2)=',len(lst2)
        lst3= [x for x in lst2][1:-1]
        print 'len(lst3)=',len(lst3)
        lst4=[]
        lst5=[]
        lst6=[]
        for x in lst3:
          lst4= x.split('"')
          for y in lst4:
            if y.find('user')!=-1:
               y=y.replace('&quot;','')
               i2=y.find('.jpg')
               if i2!=-1: y=y[:i2]+'.jpg'; lst5.append( y )
               elif not re.search('=$',y):  lst6.append( y )
#       for x in lst5: print x
#       for x in lst6: print x
        lst1=lst5 + lst6
        print 'len(lst1)=',len(lst1)
        print 'len(lst5)=',len(lst5)
        print 'len(lst6)=',len(lst6)
        h='https://pp.userapi.com/'
        j='.jpg'
        lst7=[]
#       9
        for x in lst1:
          if re.search('\\.\\.',x): continue
          if re.search('\\='   ,x): continue
          if re.search('class' ,x): continue
          y= 'https://pp'+x[:-1]
          m=re.search('\\[.{7}/.{10}/.{5}/.{11},.+,.+\\]', y)
          if m :
             ms= m.group().replace('[','|')
             ms=        ms.replace(']','|')
             mlst= ms.split('|')
             for z in mlst:
               if len(z)<7: continue
               yy= h+z.split(',')[0] +j
               lst7.append( yy )
               print 'B ', yy
          elif len(y.split('['))>=1:
             xs=y.replace('[','|'); xs=xs.replace(']','|'); xs=xs.split('|')[:]
             if len(xs)==1 :
                yy=(xs[0]+j).replace('.jp.jpg','.jpg');
                print 'A ',yy; lst7.append( yy )
          else :
             c=[h+a.split(',')[0]+j for a in xs[1:] if len(a)>7]
             for yy in c : print 'C ',yy; lst7.append( yy )
#       9
        print 'len(lst7)=',len(lst7)
        for yy in lst7 :
          if yy.find('=')!=-1: continue
          j1=yy.rfind('/')
          if j1!=-1 :
            full_path = os.path.realpath(__file__)
            jj1=full_path.rfind('/')
            if jj1!=-1:
              fn=full_path[:jj1]+'/'+yy[j1+1:]+'*'
              print 'fn=',fn
              print 'TOUCH'  
              os.system('touch '+fn[:-1])
              if not os.system('ls -l '+fn) :
                os.system('wget '+yy)
                lst9=[x.split()[-1].split('/')[-1]+' '+x.split()[4] for x in os.popen('ls -l '+fn) ]
                print 'lst9=',lst9
                os.system('ls -l '+fn)
                if len(lst9)==1:
                  print 'REMOVE TOUCH'
                  os.system('rm '+fn[:-1])
                  continue
                y0=lst9[0].split(' ')
                y1=lst9[1].split(' ')
                print 'y0=',y0
                print 'y1=',y1
                os.system('cp ../test_pix/'+y1[0]+' ../test_pix/'+y0[0])
                os.system('ls -l '+fn)
                os.system('rm ../test_pix/*.jpg.[1-9]*')
                if len(y0[1])==4:
                  print 'REMOVE SMALL'
                  os.system('rm ../test_pix/'+y0[0])
                os.system('ls -l '+fn)
#       9
#       while end
# python -c "import os;print[os.system('rm ./test_pix/'+x.split()[8]) for x in os.popen('ls -l ./test_pix') if x.split()[4:5]!=[] and len(str(x.split()[4]))==4]"


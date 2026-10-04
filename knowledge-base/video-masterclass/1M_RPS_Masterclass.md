# 1M RPS Masterclass Full Transcript

[0.08] Hey everyone, I've got a very exciting video 
for you. In this one, we're going to simulate  
[4.08] being one of the busiest routes in the world 
and handle more than a million HTTP requests  
[9.28] per second. If you think that's nothing, well, 
you're in for a surprise. This is a very high  
[14.32] stake environment here. We're talking scale of 
Uber, Netflix, and even parts of Apple and Google.  
[20.48] Just to give you some context here in the Amazon 
Web Services, their busiest service is the IAM  
[27.12] which is basically a security guard for all your 
applications and Amazon Web Services environment.  
[33.36] Now, this is the busiest route that we've got in 
the world. And this service a few years ago was  
[40.56] handling more than 400 million requests per second 
throughout the world. And this was the busiest  
[46.88] one. All right. So yeah, we don't have routes that 
handle trillions of requests. That is insane and  
[52.16] we don't have it right now, but this is something 
within reach. This is something that humanity has  
[57.44] accomplished. And in this video, we're going to 
see how close to this we can get. We're going  
[62.0] to be launching a powerful infrastructure with 
hundreds of CPU cores and dozens of computers that  
[67.36] cost hundreds of thousands of dollars a year to 
run and simulate having millions and millions of  
[72.88] users using the service at the same time. So we're 
going to be on some insane scale moving terabytes  
[79.12] and terabytes of data per minute. You're going to 
see that things are very different when you are in  
[85.04] such an extreme environment. For example, you see 
a lot of people that say the database is always  
[90.88] the main bottleneck. But not here, not here. I 
mean, you don't even want your database to be  
[95.92] your main bottleneck because the costs are just 
going to be absolutely unbelievable. You'll see  
[100.72] what I mean throughout the video. At this scale, 
a simple mistake is absolutely detrimental. That's  
[106.56] why in the video title, I said it's scary. And 
I'm not exaggerating. A simple mistake here would  
[111.92] cost your company tens of thousands of dollars. 
And a mistake here is not a bug. Having a bug  
[117.52] here is unfathomable. You don't even want to go 
anywhere close to having a chance of having a bug.  
[122.32] By mistake here, I mean going with a solution 
that is, for example, bigo notion of n instead  
[127.44] of bigo notion of log n. The concept of code that 
just works is good enough is ridiculous in such a  
[134.48] high stake environment. That mentality could cost 
a company literally millions of dollars over a  
[140.48] very short period of time. Yeah. So no room for 
error. You got to really think like an engineer  
[145.76] in this environment. The mindset of I'm just a 
programmer or just a C or a Java developer is  
[151.2] not going to work here. You shouldn't shy away 
from math. something that has a probability of  
[155.68] one over a million to happen here or has a chance 
of happening every minute. So thinking just like  
[161.44] a programmer, yeah, not going to work. You 
won't even survive more than a few minutes,  
[165.84] but you'll learn. But also, it's a lot of fun. 
Scary, sure, but also very thrilling. Kind of like  
[171.44] roller coaster type scary, but with the difference 
that you can actually crash. It takes a lot of  
[176.64] engineering, a whole lot of effort, and only very 
few companies in the world would ever get to this  
[181.92] scale of 1 million requests per second. All right. 
Yeah. So, we're gonna have a lot of fun in this  
[187.04] video. I really enjoyed making every single part 
of this video. And yeah, we're going to become  
[191.44] one of the busiest routes in the world, but only 
temporarily, only for a few hours because it costs  
[196.8] so much to run. I built this video so that you 
can still learn a lot by just watching it without  
[202.48] needing to follow on. But if you want to follow 
along, please just stick with your local machine.  
[207.04] I will give you all the repos, all the code that 
I'm going to run. So you can also do all the tests  
[211.52] on your own machine. But when I then move into 
the cloud, if you want to do the same that I'm  
[215.92] going to do, it will cost you hundreds of dollars 
if not more. And you make one simple mistake and  
[220.08] there you go. You lost 50 bucks. So please be very 
careful and you're better off just watch me. This  
[225.76] video is very polished up version. I you're going 
to see a lot of fast forwards. I had to put a lot  
[230.24] of research into it. That's why you might feel 
like that this operation is actually easy to do  
[234.96] because yeah, I'm doing all these commands and 
you're going to see that they all work. But in  
[238.96] reality, that's not really how things are. And 
yeah, one simple command is going to break and  
[244.0] your whole system is now down. It it takes a 
lot of time. So if you want to try it yourself,  
[248.0] yeah, I can almost guarantee you will take you 
many hours. And even if after all the research,  
[252.8] if I wanted to do this video live, it would still 
take probably four to five hours. All right. So  
[258.48] now, thanks to fast forwarding and video editing, 
you can enjoy this in just 2 hours. So sit back,  
[264.48] relax, enjoy this video. We're going to have a 
lot of fun and we'll also learn a lot. All right,  
[269.52] before we start though, let's make sure 
that we're on the same page. In this video,  
[273.44] we're going to see SQL, we're going to see 
Unix, multi-threading and clustering, Redis,  
[278.96] and Node.js and also C++. We're going to be using 
C++ because NodeJS at one point is just not going  
[285.12] to cut it. These technologies like NodeJS, Python, 
and Java, they're just not good enough for such  
[290.16] a high stake environment here. Every single 
bit that you can save is going to really add  
[295.36] up. And we're going to go with C++ to really hit 
this 1 million. And these other technologies are  
[301.12] not good enough. Now, you don't need to know 
C++ or even Node if you want to follow along  
[305.04] with this video. I'm going to explain everything 
in simple terms. So, don't worry about it if you  
[309.44] don't know anything about them. Also, I'm going 
to be doing these tests on Amazon Web Services.  
[314.88] But again, don't worry if you don't know anything 
about it. I could have just as easily done it on  
[319.2] Google Cloud or Microsoft Azure or even just 
set up the machines myself physically. So the  
[325.52] concepts are going to be the same all around. 
For as long as you know what a computer is,  
[330.8] you're going to understand what I'm talking about. 
I will stay away from using AWS specific terms so  
[336.56] that you can understand exactly what's going on. 
But if you're working in Amazon Web Services,  
[340.8] yeah, you will also learn a few extra things. 
But again, don't worry if you don't know anything  
[344.64] about it. I'm going to be very transparent 
throughout this video. I'm going to put out all  
[348.32] the costs. Whatever we're going to run, I'm going 
to tell you exactly how much it costs per hour to  
[353.36] run so that you have some context and you know how 
big it is and all of them will be in USD. Okay,  
[358.8] let's now talk about prerequisites. So, if you 
want to get the most out of this video and be  
[362.88] able to follow along and understand it, these are 
the basic things that you need to know. All right,  
[368.8] you need to know some basic SQL. Nothing too 
crazy for as long as you know how to select all or  
[374.32] insert or update. That's pretty much all that you 
got to know. Next, you also need to have done some  
[379.76] backend development at one point. You got to know 
what is an HTTP request, have set up maybe an API,  
[385.76] even on your test machine, not even anything too 
crazy. Doesn't matter if you've done it in Java,  
[390.4] Python, Net, whatever you've got. But you got 
to have some experience. You also need to know  
[396.48] what a computer is. And by that I mean you got to 
know your CPU, how many cores you've got, what is  
[401.68] a thread. You got to know that your memory is way 
faster than your disk, that you've got a network  
[407.12] card, that you can connect computers together 
using an Ethernet cable through the network card.  
[413.2] And again, yeah, some basic stuff. That's all you 
need to know. And also know that one bite is equal  
[418.56] to 8 bits. All right? So if you've forgotten this, 
just keep this in mind. So 1 GB is equal to 8 GB.  
[425.84] You also need to know what NodeJS is. Just know 
what it is. You don't need to have done any  
[430.56] development in it whatsoever. Just know that it's 
a system level technology that is like Java and  
[436.16] Spring and not like React. So you can deal with 
files, you can do Unix stuff, run other processes,  
[442.72] spawn threads, communicates over the network and 
other stuff like that. I also highly encourage  
[448.56] you to install it and run a simple Hello World 
application. Again, you don't need to go too  
[453.04] crazy. just play around a little bit because I'm 
going to be running some fair bit amount of node  
[457.68] code throughout this video. So if you can also 
do that that's really good. You can also then do  
[463.36] some of the tests that I'm going to do on your own 
local machine by grabbing the repository. One last  
[468.24] point, you got to know how to SSH into a computer 
and know what happens when you do it. So when you  
[472.96] SSH into a computer that's in another country, I 
want you to have a conceptual idea of what exactly  
[478.4] is happening behind the scenes. I'm going to 
be doing a fair bit amount of sshing here in  
[482.24] this video. So, I want you to know what's going on 
and also know some basic terminal commands. Again,  
[487.44] nothing too crazy. Just know how to change 
directories, make folders, delete files,  
[493.2] create files, add a file, some basic stuff, right? 
Very, very basic. And if you have all this basic  
[500.48] knowledge, you're good enough to follow along 
with this video. All right, before we get started  
[504.88] though, I want to talk a little bit about this 
CPU and threading. So, I'm going to now talk about  
[510.0] core utilization and also CPU utilization and 
two different methods that we've got to calculate  
[515.76] them. We're going to be doing a whole lot of 
resource monitoring at this scale. If you are not  
[520.64] doing resource monitoring, you're doing it wrong. 
There is no way that you can accomplish it without  
[525.12] doing a crazy amount of resource monitoring. So, 
I want to make sure that you understand all these  
[529.44] numbers that we're going to see. We will then 
go ahead and spawn a few threads on our machine  
[534.64] to make sure that we really understand this CPU 
utilization. So if you feel like you know all this  
[540.32] stuff, please use the progress bar down below to 
skip right ahead and start this video. All right,  
[545.92] so now I'm going to talk about this resource 
monitoring. Let's start with core utilization. So  
[552.64] your CPU, it's got multiple cores. You can check 
it out right now. Please pause the video right now  
[557.2] if you don't know how many cores your CPU has 
got. Go and Google it. There are some commands  
[561.28] that you can run on Windows, Linux, and Mac to 
get a number of how many cores you've got. Now,  
[565.76] a single core utilization formula is this. It's 
very straightforward. You take the total time,  
[571.2] any span of time that you want. For example, 
the last 30 minutes, and you also know the total  
[577.12] idle time. This means that throughout that last 
30 minutes, how long the core was doing absolutely  
[583.84] nothing. So, each core can either do something or 
not do anything. All right? that doing something  
[589.28] could be a simple operation of adding two numbers 
together or checking if something is true. All  
[593.76] right, so some basic stuff but idle time means 
that the core is doing just totally nothing.  
[599.36] Just sitting right there and relaxing. So you 
take this then you divide this by that total  
[604.96] time and then you multiply by 100 and then you 
get a core utilization. Very straightforward.  
[609.6] So let's say that in the last hour the total 
idle time of a particular core was 30 minutes.  
[615.28] So you plug that number right here and you're 
going to get 50%. Meaning that that core was  
[620.32] utilized 50% of the time throughout the last 
1 hour. All right. Now CPU utilization because  
[627.28] again remember your CPU has got multiple cores. 
Very straightforward. All you need to do here  
[632.96] is take each core utilization and add them all up 
together. And optionally you can also divide this  
[639.92] by total number of cores. So this last division 
is optional. Some systems do it, some don't. And  
[647.04] you can actually also specify if you want to 
see this or not. So, we've got two different  
[652.24] methods to display CPU utilization. One is to just 
add all the core utilizations and that's it. In  
[658.16] this case, in method one, you're going to get a 
percentage that's higher than 100%. For example,  
[662.88] if you've got four cores and you're utilizing 
all four, the CPU utilization is going to be  
[667.68] 400%. But in method two, it's always a number out 
of 100. So in that case of four cores being fully  
[674.64] utilized here using method two, we're going to get 
a number of 100%. Very straightforward. All right,  
[681.2] let's see this in action. Please go ahead and 
grab this repository. The link is going to be  
[685.36] in the description box down below. We're going to 
have three repositories here for this video. This  
[690.16] is one of them. This is our code in Node. And then 
we're going to have another one in C++. All right,  
[695.28] but here if you grab it in the playground, don't 
worry about all the other folders. We're going  
[699.6] to get into them in just a bit. Here I've got two 
files. One is called singlethread.js and all it's  
[705.28] got is a simple while true. All right. So if you 
don't know node, go ahead and run this in your  
[711.44] favorite language. Be it Python, Java, doesn't 
matter. Just put a while true and then go ahead  
[716.8] and run that code. So I'm going to go ahead and 
do it here with Node.js. You can run files by  
[723.28] just saying node and then specify that file which 
is here in my playground and then single thread.j  
[729.12] JS. All right. So now I'm running this and then 
go into your system monitor. All right. So here  
[735.04] on Windows that will be task manager. On Linux 
that'll be system monitor. Here on Mac that will  
[740.8] be activity monitor. And then search for the 
process that you just ran. Here with node it's  
[745.76] simply called node. So here's the process. And 
then I want you to take a look at the CPU usage.  
[751.6] Right? you're going to see that it's 100% if it's 
using method one that we just talked about or it's  
[757.04] another number if your system is using method 
two to report the CPU usage. In that case, for  
[761.6] example, if you've got four cores here, you should 
see 25%. All right. Now, also monitor your total  
[768.24] CPU utilization. So, here this is now my total 
CPU. I've got 12 cores and you can see that the  
[774.56] idle CPU is now around 70%. All right, a little 
bit amount of it is now going towards my video  
[780.8] recording and also a good portion is going towards 
this Node.js process. Right? So I really want you  
[786.08] to understand these numbers that you've got. 
Now system and user if you add them together,  
[790.88] this is going to be the total CPU utilization. 
The idle here is again referring to the total  
[795.68] CPU that's not being utilized. All right, 
so all the cores added together. All right,  
[800.0] so that's the first example. This is running in 
a single thread. All right. Each thread can only  
[805.6] utilize one CPU core at any given point of time. 
So here in this code, I cannot do two things at  
[812.0] the same time. I cannot go right ahead and say 
add two numbers simultaneously. Right? I could do  
[818.72] something to make it seem like that it's actually 
adding them together, but my CPU is doing one and  
[823.84] then doing the other immediately after. If I want 
to do two things exactly at the same time so that  
[829.2] I can speed up my program execution by about 
two times then I need to spawn another thread.  
[835.76] All right. So here I've added another piece of 
code multi-thread.js. Again grab this code. Go  
[842.24] ahead and convert it into your own favorite 
language. You can do this with Python, Java,  
[847.92] C, C++, what have you. And here what I'm doing is 
that I'm spawning 12 threads and I'm doing again  
[856.08] the while true in each individual thread. All 
right, very straightforward. So now I am doing  
[863.28] 12 things at the same time, not just one. Now 
theoretically this would really speed up your  
[869.6] application because now you're utilizing all 
your CPU, but you also got to worry about things  
[874.4] like race conditions. You got to use sometimes 
semaphors and so many other things to make sure  
[879.52] that your program is going to work properly. But 
also in some cases you just don't need to worry  
[883.68] about it. You call a function and the developers 
who made that function have already taken care of  
[888.32] all those things for you. All right. So let's go 
ahead and run this code. Again here I'm spawning  
[893.44] 12 threads because I know that my CPU has got 12 
cores. In your case, you should know by now how  
[899.04] many cores your CPU has got. So change this 
number to that. If you've got eight cores,  
[904.08] go with eight. If you've got maybe 32 cores, 
go with 32, right? Okay. So now I'm going to  
[910.8] go ahead and run this one. So node playground and 
then multi thread.js. All right. Once you run it,  
[916.48] it can immediately go into your activity 
monitor or system monitor, whatever you've got,  
[920.72] and check your CPU usage. Now, for this process, 
you can see that the percentage is 900%. Now,  
[927.04] ideally, without the video recording, it's going 
to be around 11,00%. But because I'm also doing  
[932.16] a whole lot of recording and some other stuff 
in the background. So, I've got a lot going on  
[935.76] here. But still make sure that you understand 
this number. This is now being reported using  
[940.72] method number one. So, this method. Now, let's 
also take a look at our total CPU usage. So,  
[947.52] down in the bottom, you can see that my idle CPU 
is now 0%. All right? It's not 0.1 or 0.2, it's  
[953.92] exactly zero because all of my cores are now being 
fully utilized. they don't get a chance to breathe  
[960.4] because I've also got some other processes going 
on. So everything is now working. I've got a whole  
[965.92] long queue of operations for my CPU to run. So 
it's not getting even a single chance to breathe.  
[972.16] All right. All right. So again, I want you to 
understand that here we're running 12 while loops  
[977.52] at the same time. All right. So just make sure 
that you understand this concept and that also  
[981.92] you understand what exactly is going on here. I'm 
going to shut this down so that my recording is  
[985.84] not going to get tampered with. But yeah, that's 
it about CPU utilization and multi-threading.
[996.8] All right, let's get into it. So, let's start from 
something very, very simple. I have this project  
[1003.92] here called 

... [OUTPUT TRUNCATED - 117,843 chars omitted out of 167,768 total] ...

05.92] and we have 60 of them. So per month this 
costs $20,000 just for the testers. All right,  
[7914.0] or about 30 bucks an hour or 40 bucks I guess with 
that beast server in place. All right, so here I  
[7920.08] have created a bash script. You can rewind and 
pause the video if you want to take a look at it,  
[7923.68] but basically all it does is that it's going to 
send the autocannon to all these 60 machines and  
[7929.76] then it's going to grab the output. All right, so 
yeah, here I'm trying to figure out what values to  
[7935.6] go with. So I went here with a very low connection 
count. Yeah, here you can take a look at the  
[7942.0] result that it actually works and I got the output 
of all the machines. Now you do see the error but  
[7947.36] that's because autocannon outputs to standard 
error by default. All right. Yeah. So it works.  
[7953.68] In 20 seconds, you can see that we still handled 
about a million requests with that machine per  
[7959.36] second. So now at this point I'm feeling kind of 
confident that, all right, do this works. Let's go  
[7965.76] for that final big test. So here we can see that 
connections 800 and I'm going to now change the  
[7973.28] duration to something much higher. All right. So, 
instead of going with 3 minutes, we're going to go  
[7978.4] with 1 hour. All right. I'm feeling excited, hyped 
up... that this is just going to be insane. Like,  
[7985.36] the amount of traffic that we're going to send is 
just mindblowing. All right, so here I've got the  
[7992.0] server. I'm getting ready to hit enter and do this 
final insane test. All right, there we go. Now,  
[7999.04] the tests are running. 60 machines are sending an 
insane amount of traffic over to this beast. All  
[8005.84] right, so here's what's actually happening. 
We've got 60 computers here and they are all  
[8011.84] sending traffic, bombarding this beast server 
with an unbelievable amount of traffic. Now, if  
[8017.84] you want to know how many requests per second this 
machine is handling, take the number of servers,  
[8023.04] which we've got 60. each one is opening up say 
maybe 400 connections and then pipelining of five.  
[8030.16] So we multiply them all together we end up with 
120,000. Now this number is how many requests in  
[8037.2] any given time this server is handling. All right 
in total we have 60 * 400 connections opened up  
[8045.76] to this server. All right I'm not going to draw 
all the lines but you get the point. So all these  
[8050.4] computers are now simultaneously sending lots 
and lots of traffic here to this machine. Each  
[8056.48] one with 400 connections opened up. All right. 
Yeah, I'm going to try it with a few different  
[8061.68] values and the server is just going to handle 
all of them. We will get a few timeouts when the  
[8066.0] connection goes way too high. But yeah, this is 
crazy. 120,000 at any given point of time is like  
[8072.48] having millions of people using your application 
at the same time. Absolutely mind-blowing.  
[8078.48] All right. So back here we can take a look and see 
running this script for 1 hour and also connection  
[8084.96] count 800 the CPU usage of the idle machine is now 
0%. So at the top right hand side I've got the CPU  
[8092.0] usage of the server. Top left side I've got the 
server running and then the bottom terminal is  
[8097.36] my local machine. This is where I'm running that 
bash script from to utilize all these servers at  
[8102.64] the same time. Right. So here I'm going to let 
my recording go for 1 hour. do all this testing.
[8112.08] Now, here I'm trying to just check that it 
works fine because you got to double check  
[8116.0] because we're sending lots and lots of traffic. 
Yeah, you can see that it took a little bit amount  
[8120.08] of time for it to respond 1 second, but that's 
expected. Now, this next one was way quicker. So,  
[8125.12] the server is working fine. We're not getting 
any errors and at the same time it's handling  
[8131.28] more than a 100,000 actually quarter a million 
in this case. quarter a million requests at any  
[8137.12] given point of time, handling more than a million 
per second. Absolutely massive. Now, it would also  
[8142.24] be interesting to see how much electricity we're 
using in this test. If you count in the CPU, we  
[8146.96] know exactly the type of CPU, the wattage. We also 
know that we're moving terabytes and terabytes  
[8152.08] per minute. It's it's a whole lot of traffic. I'll 
give you a complete output later in the video. So,  
[8157.6] take that, do some math, and see how much 
electricity we're using. Hopefully, someone  
[8161.84] can do that. But I did a bit myself. And with 
the electricity that we're using here in 1 hour,  
[8167.12] we can power a Tesla car to run for thousands 
and thousands of kilometers. It's no joke. It's  
[8173.04] a whole lot. All right. So, back here. Yeah, I was 
really disappointed. The test was finished and the  
[8179.36] server handled it all okay, but you can see that 
the logs were actually really, really messed up.  
[8184.56] So, I was feeling so sad, so angry that what the 
heck just went wrong? Why can't I see the rest of  
[8189.28] the logs? I tried to troubleshoot, but at the same 
time, these machines, they cost about 50 bucks  
[8194.399] an hour, 40 bucks an hour. And yeah, it's kind 
of stressful to try to debug at the same time,  
[8199.68] you know, that that's going on in the background. 
So yeah, I just wanted to give up now and say,  
[8203.6] "All right, we can't get the logs." Here 
we can see that I'm going to try it again  
[8207.84] with 20 seconds and I get the logs. And I didn't 
restart the machine. It's still just like before,  
[8214.319] but for 1 hour, I don't know, man. Just something 
happened with 1 hour that couldn't make me get  
[8219.6] the logs again. I tried it with 30 minutes, 40 
minutes, still got the logs, but for 1 hour, yeah,  
[8226.24] this just didn't work for 1 hour. And I'm guessing 
it's something that has to do with autocannon and  
[8230.319] also the tester machines. And actually, I'm going 
to try it again, but with a different approach.  
[8236.319] And that's now coming up next. So this next 
portion is now the next day. All right. So now see  
[8241.76] the final rounds of tests. Now that one is going 
to work. So enjoy and I'm going to now tune out.
[8250.96] All right, let's go ahead and run one final 
test. So this time we're going to get some  
[8256.479] clean logs. So I've gone ahead and relaunched the 
60 servers that I've got from another image that  
[8263.2] I created. So this time what we're going to do is 
instead of running Autocanon through the terminal,  
[8268.479] we're going to run a script of autocannon. 
All right. So I'm now here in the node script  
[8273.359] including the autocannon. It's all the stuff 
that we had before. But now I'm grabbing the  
[8277.84] connections duration and all the other stuff 
here from the terminal. So this is how we're  
[8281.84] supposed to run it with a few arguments that 
they have to be in order and also our host and  
[8287.84] it's going to run it. So here with this config 
that I'm passing then the connection count and  
[8292.319] whatnot. And then here with the autocanon we're 
calling the function passing that config and  
[8298.0] then once it's done running we're going to get our 
result. So what I'm doing I'm saving this result  
[8303.439] to a file called results.txt and also append a 
few afterwards like for example the time that we  
[8311.12] started and also the time that we finished because 
I realized in the previous test that sometimes the  
[8316.64] machines wouldn't start the test all at the same 
time and it's problematic. We want all these 60  
[8321.92] machines to start running the test immediately 
at the same time. So with this we can ensure  
[8327.28] that that actually happened. So I've created a new 
repo for it called 1M- RPS tester. And all these  
[8334.16] testers here already have it. So if I go right 
ahead and SSH into one of these. So I'm going to  
[8339.92] copy the DNS. And then here I'm going to go ahead 
and SSH into that. So here I've got that folder  
[8349.92] and also this file called patch.js. So we can go 
ahead and run it. I'll just copy paste this one.  
[8356.88] So I'll say node tester patch and then specify a 
few arguments and I'll run it here. So I'm going  
[8362.88] to go ahead and run it. We're going to get this 
log and then after about 20 seconds it should be  
[8368.0] completed here in the server logs. All right, 
there we go. So, the server is now kicking in,  
[8372.72] handling a few requests, but the idle is a lot 
because one single server here can't really do  
[8377.76] much against this massive beast. So, yeah, let me 
wait for it to finish after 20 seconds. All right,  
[8384.319] we got a bit of an error here with the output 
file. I'll go right ahead and run it as pseudo.
[8392.8] All right, it's now done. So, if we take a look 
at the results, so we're going to get this file  
[8397.52] and that's pretty much it. So all these same 
tables that we had as before and also when the  
[8403.359] test started and finished and some of these other 
variables here at the bottom. All right. So with  
[8407.92] this in place, let's do the final test now. All 
right. So I want to go ahead and copy command.  
[8414.8] Paste that right here. And don't be afraid of this 
command. All it means is to send this command. If  
[8420.64] you take a look here at my parameters commands, 
I'm saying cd into this folder and then run node  
[8427.28] 1 million rps patch.js with these parameters. 
All right, here this document name AWS run shell  
[8433.92] script. As the name suggests, we're going to 
run this shell script. All right, and then this  
[8438.479] max concurrency 100%. This is going to now ensure 
that this command is going to be sent to all the  
[8444.08] 60 servers at the same time. Yeah, I've learned 
this the hard way because by default, this command  
[8449.04] only sends them to 50 servers, then wait for them 
to finish or wait for a bit, and then send to the  
[8454.56] next 50. All right, but we don't want that. We 
want all these 60 servers to start immediately.  
[8460.0] And then here, I've added two more things. This 
is an S3 thing, which is basically just a file  
[8465.68] storage in Amazon. All right, so I'm saying to 
grab the output and then save it to that. And then  
[8471.76] also this cloudwatch is pretty much like that. 
It's something that we can use for logging and  
[8475.52] watching our resources. All right. And the reason 
that we can actually do this from our terminal  
[8480.56] send one command to all the machines and tell the 
machines to output now to this S3 storage. The  
[8486.72] security guard for all of them is IAM the busiest 
service in the world that we talked about at the  
[8491.92] beginning of the video. It's a really phenomenal 
service. It allows us to do all these different  
[8496.56] operations. Of course, I also had to configure 
IAM to give enough permission to the instances  
[8501.6] to actually be able to output to these different 
places. Okay. And then at the end, I'm just saying  
[8507.68] to give me the command ID. You'll see why. So, I'm 
going to go ahead and run it. And that's now fired  
[8512.96] up. So, all my testers should now be sending lots. 
Oops. Actually, the second argument here is the  
[8519.76] duration. And here I specified only how much? 180. 
So, it's only 3 minutes. You know what? Let me  
[8527.439] cancel this command using this AWS command. Cancel 
command. And I'll copy my command ID. That's why  
[8532.8] we need it. I want to now go ahead and cancel this 
run. And now the CPU usage of the server should go  
[8537.92] back up to 100%. All right. And I want to go ahead 
and run that again because we want to do a little  
[8542.8] bit more. All right. We want to do a bit more than 
3 minutes. And I'll change this from 160 to 1,800,  
[8550.8] which is 30 minutes. All right. So now we're going 
to run this test for 30 minutes straight and then  
[8558.08] see what's going to happen. All right, there we 
go. And also there's another command that I can  
[8563.84] run here. So I'll run AWS logs tail and then 
aws/sm/benchmarks and then --follow. With this  
[8576.399] in place, I can now follow the output of all my 
60 servers. Right? So here if you take a look it  
[8583.04] shows me that yeah each server you know that log 
that we just saw in an individual one. So here  
[8588.8] I'm specifying to tail this so follow this one and 
I'm also specifying that here in my cloudwatch. So  
[8595.12] here if you take a look that's my group name which 
is pretty cool you know from my own terminal on  
[8599.52] my machine I can mobilize all these 60 machines 
and take a look at the output here in real time  
[8605.76] in my own terminal. Pretty cool stuff. Okay, so 
now I'm going to wait for it to finish. So I'll  
[8612.0] wait another 30 minutes. I actually ended up 
running this architecture of 60 servers for for  
[8618.0] a few hours. It's been costing quite a lot. We've 
been moving hundreds and hundreds of terabytes in  
[8623.92] a few hours. It's a lot. But let's do one final 
test. 30 minutes the final one. And then we're  
[8630.8] going to end up with a very cleaned output 
structure. Now, while this is also running,  
[8636.56] actually while I'm recording this video, I got a 
message back from Amazon. So, if you recall before  
[8642.399] I mentioned that I ran this test, I didn't show it 
in the video, but I ended up having a beast tester  
[8648.16] and a load balancer. And this is a network load 
balancer. It operates at the TCP level and not  
[8653.439] the HTTP level. So, this is very fast. And also, 
I'm putting it on the same private network. Okay.  
[8661.2] And I thought now with two beast servers, we're 
going to be able to handle way more requests.  
[8666.319] Well, that's not what I saw. I actually saw a 
very degraded performance here with this load  
[8671.28] balancer. I tried to troubleshoot. But I saw it 
was taking a little too long because the setup is  
[8676.88] not cheap to run. So, I decided instead to reach 
out to Amazon and see what they have to say.  
[8682.72] So here in the support center of Amazon, I sent 
them this message that I have two of these beast  
[8689.04] servers and I utilized both and long story short 
here I have also added two attachments individual  
[8696.72] benchmark and then one with the load balancer. 
So let me pull them up right now. So in the top  
[8702.0] I've got the individual. You can see that I was 
handling 1 million per second. Now here, this is  
[8708.399] now with the load balancer. You can see it's now 
down to only 5 GB per second. It's way lower than  
[8714.64] what I had here with this. And I reached out to 
Amazon to see what the heck is going on because  
[8720.479] they actually advertise the network balancers as 
this powerful thing that could handle millions of  
[8726.24] requests. Right? So I said this is what you 
guys say, but I did not see that in action.  
[8730.88] So they reached out to me and now this is just 
to indicate that someone is working on it. But  
[8736.08] here's the actual response that I've got. Someone 
reached out and said that based on our metrics,  
[8742.319] the consumed load balancer capacity reached 165, 
which was the limit. All right. And if I want more  
[8750.399] traffic, I got to reserve this in advance. I need, 
you know, I need to say that I want more capacity  
[8756.08] than what I've got. All right. So, if I don't do 
that, this load balancer is not going to be able  
[8761.6] to cut it. So, we got to reach out again and say 
that I want to reserve this in advance to move  
[8766.88] such a mind-blowing amount of traffic across. The 
traffic that we're moving is at the scale of Uber  
[8772.24] and some big companies. So, yeah, sure, we might 
see some limitations here and there. They also  
[8778.319] told me to do some operations, but I have already 
actually done them and I still did not see much of  
[8782.64] a difference. So, I did all of that and then ran 
a few more tests and still saw the same things.  
[8787.52] They also gave me a few links here which I found 
quite useful. So here with this we can actually  
[8793.2] now reserve capacity right so I'm going to have 
to say that I want for example 600 gigabits per  
[8799.2] second and number of connections maybe we want 
100,000 and availability zones maybe one and  
[8807.04] then it's going to tell us how many LCUs we need 
this is actually application load balancer so I'm  
[8812.319] going to have to switch to network balancer 
and say that I want maybe 300 and maybe one  
[8817.439] availability zone and here's the number that I'm 
going to get so I need to say for this much or  
[8822.319] maybe for this much I need to reach out to Amazon 
and say give me this much capacity for my for my  
[8830.72] application. I'm not so sure here how much this 
would cost but yeah this is pretty interesting.  
[8835.76] I did not know this actually before this test. And 
then here's a little bit more on it. So if you're  
[8840.72] interested feel free to go ahead. So yeah, that's 
what we can do to really put this into test and  
[8846.0] utilize the two beasts fully. But I'm not going 
to do it again. This this costs a lot of money  
[8851.6] to run. Moving terabytes and terabytes per minute 
is actually very costly. So, I'm not going to do  
[8857.439] and follow along with this, but it's really good 
to know. And thanks Amazon for reaching out with  
[8862.399] this. They really responded pretty fast because I 
ended up getting the business support for it. They  
[8867.04] also had to run an AI for me for for a few minutes 
to see if the AI could solve the problem. Gave  
[8872.56] me like 10 suggestions, but none of them ended up 
working. Yeah, at this scale even AI really can't  
[8877.76] help you much because only very few companies 
handle 1 million per second. So I'm guessing  
[8883.28] AIs did not have enough data to get trained on for 
such a massive scale. But the human response here  
[8891.2] was really good. Now let's go back to our tests. 
So here we still have it running and our logs.  
[8898.72] So we may need to go for a couple more minutes. 
So I'm going to go ahead now and fast forward.
[8921.68] All right. So, as you can see right now, the tests 
are completed. Let's go ahead and take a look at  
[8927.28] the results. Now, because we have saved all these 
into that results.txt file. What I could do here,  
[8935.84] if you take a look at the output, all the 
machines outputed that the test completed  
[8939.92] and results saved here to results.txt. Now, 
here I'm going to paste another command with  
[8945.92] AWS SSM and say to run cat results.txt on all 
these machines. All right, where I've got the  
[8954.56] name of tester and then also save the output here 
to S3, so our file storage. So, I'm going to go  
[8961.28] ahead and run this. If I take a look at the live 
result here, we can see that I get all of them,  
[8966.24] right? Which is pretty cool. But let's go ahead 
and concatenate all of them together because yeah,  
[8971.52] this was a massive test. So, I want to make sure 
that I have the results. Now, here, here's the  
[8976.64] S3. I'm going to go ahead and show you that. If I 
go into the storage, it's basically just storage  
[8982.8] in the cloud. And that's it. I've got a bucket. 
Don't worry if you don't know what a bucket is,  
[8987.04] but just like a folder, right? And then yeah, I 
ran a few tests here, but if I take a look at my  
[8993.359] command ID, right? So this one, this is now my 
folder name, which starts with 97. So let me see  
[9000.319] if I can find that. There we go. And then inside 
I've got the output of every individual instance.  
[9006.399] So if I go there and then another folder and then 
another one here, I can see the standard out. So  
[9012.0] if I open it up, I can download it. And here 
we go. Pretty cool. Now, we want all of them  
[9018.399] to be in a single file. So, let me now show 
you the power of bash scripting. All right,  
[9024.0] let me minimize these and then make this bigger. 
So, I'm going to first download the S3 folder. So,  
[9030.319] I'm going to have to use this command AWS S3. 
Specify my URL here. I want to click on copy S3  
[9038.0] URI. So with this I can now paste that here with 
this one which is the command ID. And I want to  
[9045.84] say to save this into my current directory into a 
folder called results. I'm missing a sync here. So  
[9053.28] I need to save this and then run it. And it's now 
going to download every individual folder and put  
[9058.88] it here into that results. So here I've got all 
these folders in a very clean way and I can see  
[9065.359] the result of every single individual one. All 
right. Now with bash scripting I can very easily  
[9071.68] concatenate them all into one file. So I can say 
find everything here in this results folder that  
[9079.359] path is like this. So star meaning everything and 
then standard out and then execute. So I'm going  
[9085.359] to have to now say concatenate all of them. So cat 
and then yeah don't worry what this means. It just  
[9090.8] means to cat every individual file and then put 
all the output here into this file. And I'm going  
[9095.92] to call this 30min-60 meaning 60 instances and 
then results.txt. I'll go ahead and run it. And  
[9105.68] now if we take a look here, you can see that 
I've got all the results here in a very clean  
[9111.84] file. It's very cool. I will also put it out on 
GitHub. So if you want to take a look at it and  
[9116.16] do some math, but let's make sure that we've got 
60 results. So 60 of tests. In a few of my tests,  
[9122.64] a few of them were missing. But now with this one, 
we should have all of them here. If I grep read,  
[9128.64] grep means just grab a line that has a read 
here from this file. All right. So, yeah,  
[9134.24] I get all of them, but let's count. If we count 
all of them and we get to 60, that means that  
[9139.28] we've got all the results. So, I'm going to use 
the WC command and say -l to give me a number. So,  
[9145.359] we've got 60 lines, meaning that we've got 60 
result outputs. Each one ran for 30 minutes. And  
[9152.64] you saw that the server did not break a sweat. It 
handled all of them with no errors whatsoever. We  
[9158.8] also didn't get any errors. So if I go ahead and 
grep error or errors, I think it's called should  
[9165.84] be called errors. Yeah. Oh, actually, yeah, we do 
have a few timeouts, but only 40. All right. So,  
[9171.28] if I take a look at them here, and sometimes 
we do get some timeouts, sometimes we don't.  
[9178.8] But over millions and millions of requests, we 
only ended up with 40 timeouts, which is pretty  
[9184.64] impressive. And keep in mind that we were opening 
a 100,000 connections to the server, sending that  
[9191.439] much at any given point of time. Yeah, this was 
this is quite insane. Now, let's go ahead and  
[9197.52] do a few more bash scripting here. What I could 
do is to say again, grep read all. Let's see how  
[9203.2] much data in total we actually moved across. So, 
I'm going to actually use the awk command here.  
[9208.319] It's very powerful. If you don't know bash 
scripting, you're missing out. You're losing a lot  
[9212.319] of time. So, go ahead and learn it, please. So, 
I'll say here, I'm going to give it req plus the  
[9218.08] first argument of that. And then data. And this 
one, it should be the fifth argument. So, 1 2 3 4  
[9225.2] 5. All right. Say dollar sign five. And then after 
it's done, I'll go ahead and print total requests.
[9238.399] And here I'll put in a req and then a K. And 
I'm also going to print the total data read.  
[9248.08] So my variable I called it data before. And 
then this is in terabytes. So I'll put a TB  
[9253.52] right here. And this should actually work. There 
we go. So, in 30 minutes in total, all right,  
[9261.68] let's take a look at this. We sent two billion 
requests. All right, two billion. This is a whole  
[9267.84] lot. And we also moved across plus 60 terabytes 
of data. This is absolutely mind-blowing. 60  
[9276.08] terabytes and two billion requests were handled 
by this beast machine in just 30 minutes. And we  
[9283.12] could have gone with one hour. Just just multiply 
these two numbers by two and that would have been  
[9288.08] the result for 1 hour. This is astonishing. 2 
billion. And out of two billion requests, we  
[9294.319] only ended up with 40 timeouts. Pretty impressive 
stuff. Yeah, this this beast machine is insanely  
[9303.84] powerful. Along with C++ and Drogon, you can do 
whatever you want. It handles so much and it's  
[9311.04] yeah, it's really cool to see this in action. 
And that concludes it for our final big test.
[9321.12] All right, and that's it about this video and us 
handling a million requests per second. Thank you  
[9326.72] very much if you've been following along until 
this point. I really appreciate all the support.  
[9330.64] It means a lot. Hopefully, this video gave you 
some new perspectives on software engineering and  
[9335.84] how to go about it and also improve your thinking 
process a bit. And that was my goal here with this  
[9341.04] video. it was not to show you how to set up an 
architecture to handle a million requests per  
[9345.76] second. Well, every one of these topics that we 
talked about here would require hours and hours  
[9350.64] of dedicated content. And my goal wasn't really 
to do any sort of how-tos in this video. I think  
[9356.399] the age of how-to videos is pretty much over 
at this point with AI taking over, especially  
[9361.28] in software development. So, that's also the 
direction that I've been moving my content  
[9366.24] towards in the past few years. I'm trying to build 
content in a way to improve your thinking process,  
[9371.28] make you a little more creative, and give you 
new perspectives, and not just to show you how to  
[9375.92] do this or how to do that. And hopefully I'll be 
able to live up to that because it's so much more  
[9381.28] difficult to create content like that. This video 
was a lot of fun for me to make. All these tests,  
[9387.28] all the research that I had to put into it 
were a huge amount of fun. Also stressful,  
[9391.6] but very, very fun. If you were curious to know 
the cost for this month, it's around $2,000. Now,  
[9398.08] not all of it is actually for the tests that 
I conducted throughout the video, a lot of it  
[9403.76] is again the research that I had to put into it 
and not all of it is specifically for this video.  
[9410.16] We have around $800 for databases and around 
$1,200 for EC2 compute. Now, in hindsight, yeah,  
[9416.8] if I were to go back, I would be able to cut this 
cost down by a few hundred. I did make a few silly  
[9421.92] mistakes that ended up adding a couple hundred 
dollars to the bill, but it could have been  
[9426.399] worse. It could have been way, way worse. Now, 
if you want to get more involved with us here,  
[9431.12] check out this URL shortener app project. It's 
open source. We're not going to be doing any vibe  
[9436.08] coding here or use any AI generated code or any AI 
slop. We're going to have a lot of fun with this.  
[9441.2] We're going to be learning a lot. Let's see if 
we can shorten 1 million links per second. That's  
[9445.92] going to be a massive challenge. and 1 million per 
second here is going to be way more difficult than  
[9451.84] this video because here we've got real business 
logic. We've got so many tables, complex logic,  
[9457.92] we've got authentication, encryption, and it's 
going to be it's going to be so fun, so epic. So,  
[9464.0] we're going to be trying this, but it's going to 
cost even more. And we're going to have a lot of  
[9468.88] opportunities here to learn, but we're still 
months away from being able to do that because  
[9473.28] we're building this with Cpeak and still a lot of 
features that need to be completed for release.  
[9479.76] But yeah, we're going to be learning a lot. We're 
going to hire some attackers to constantly attack  
[9484.0] this application, try to hack it, and because 
we're also building the framework ourselves,  
[9489.439] we're going to have a lot of opportunities here to 
learn about security, about designing performant  
[9494.319] code, and so much more. If you get involved 
with these two projects, that's going to give  
[9499.2] you more opportunities to learn than any AI or 
traditional course can ever offer. Because here  
[9504.72] we are building for production. We're building 
for real people to end up using this product  
[9509.04] and not just technical people. We want people 
who don't know who we are to end up preferring  
[9514.16] this one over the rest of the applications. And 
we're building for the real world and not just  
[9519.84] for education or anything like that. And in that 
environment, things are very different and we're  
[9524.96] going to have a lot of opportunities there to 
learn and become better engineers. There's also  
[9529.76] our Node.js course. Now, this one is paid, but 
if you can check it out, it would mean a lot.  
[9534.24] I would really appreciate the support. And again, 
thank you very much, and I hope to see you soon.
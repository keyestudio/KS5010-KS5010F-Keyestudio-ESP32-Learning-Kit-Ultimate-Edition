# Getting started with C (Raspberry Pi)


## About raspberry pi：

Raspberry Pi is a card computer whose official system is Raspberry Pi OS, and can be installed on the Raspberry Pi, such as: ubuntu, Windows IoT. Raspberry Pi can be used as a personal server, performing camera monitoring and recognition, as well as voice interaction by connecting a camera and a voice interactive assistant. Also, Raspberry Pi leads out 40Pin pins that can be connected to various sensors and control LEDs, motors, etc. This can be used to make a robot with a Raspberry Pi.

## Install the Raspberry Pi OS System：

### 1. Tools needed for the Raspberry Pi system：

#### 1.1. Hardware Tool：

（1）Raspberry Pi 4B/3B/2B （2）Above 16G TFT Memory Card （3）Card Reader
（4）Computer and other parts

#### 1.2. Software tools that need to be installed：

**Windows System：**

##### **（1）Install putty**

Download link：[<span class="underline">https://www.chiark.greenend.org.uk/\~sgtatham/putty/</span>](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

![](media/c26be4cd1f5543f20f275556ce5892c0.png)

![](media/d888918aa7bf9e5ea94597aad1ee4224.png)

1.  After downloading the package file ![](media/e597704d7033c7c3c5da06d4f561822c.png), double-click it and tap “Next”.
    
    ![](media/01f1b2d98915be2be9c0c2a3d330dde2.png)
    
2.  Click “Next”.
    
    ![](media/bd698753a8eea7a2ff5c5e0e598cbd94.png)

3.  Select“Install Putty files”， and click“Install”.
    
    ![](media/071a0acc98bb2dc5cd45d85dec72d111.png)

4.  After a few seconds, the installation is complete, click "Finish".
    
    ![](media/ec368c3a549c09edd70f9786456d5430.png)
    

##### **（2）Remote Login software -WinSCP**

Download link：[<span class="underline">https://winscp.net/eng/download.php</span>](https://winscp.net/eng/download.php)



After downloading the WinSCP software file, double-click the WinSCP software file![](media/1719daa1002d7477ad4700e1df85d2df.png) and
click![](media/1719daa1002d7477ad4700e1df85d2df.png).

![](media/5ee80ade909fe3eb73dc9535704b4c0b.png)

Click“Accept”，then select the appropriate option and click“Next”, then Click“Install”.

![](media/9c652f54f6a7d53f6b2aedba40104a00.png)

![](media/f32891714d5966037d59d1812aa15686.png)

![](media/57d6139ba0aac9ca996bcbe6f6fd218f.png)

![](media/49ffed878ee84546b156af3a0bf5556e.png)

After a few seconds, the installation is complete, click "Finish".

![](media/14ffa1e11243835d30ffb933219dcef5.png)

##### **（3）Format TFT card tool-- SD Card Formatter**

Download link：

[<span class="underline">http://www.canadiancontent.net/tech/download/SD\_Card\_Formatter.html</span>](http://www.canadiancontent.net/tech/download/SD_Card_Formatter.html)

![](media/fa229f4e063572ce1c59574c308bf452.png)

![](media/ac5d5eb9463805484b9239b99faf04eb.png)



Unzip the SDCardFormatterv5\_WinEN package and double-click the SD Card Formatter file![](media/8c6f8da97bf702080a8e302db2e9f982.png) to run it.

![](media/046c67e4072093ee3dad27e8088fcf9f.png)

Click“Next”，select“![](media/13dc08ae2b5cb52ae3d7ea198134d778.png)”and click“Next”.

![](media/384203e0b54ddfe37f18b65f70e786e5.png)

![](media/cf4e91eac0c0573cff282256a915a01a.png)

Click “Next”again, and then click “Install”.

![](media/0af58ee3afb14005a884ca2dc941157f.png)

![](media/807623ddeea20c8b61503845d8aec9bc.png)

After a few seconds, the installation is complete, click "Finish".

![](media/df2deb7e04c25ee207e994f0d2808194.png)

##### **（4）Burn mirror system software tool--- Win32DiskImager**

Download link：[<span class="underline">https://sourceforge.net/projects/win32diskimager/</span>](https://sourceforge.net/projects/win32diskimager/)

![](media/4ffb55fd466198ca9524afbde7806271.png)



1.  After downloading the software file![](media/63c3eaf215c92c325f95613c9d8d49ce.png)，double-click Win32DiskImagersoftware file![](media/63c3eaf215c92c325f95613c9d8d49ce.png)，and then click“Run”.
    
    ![](media/0f86f055a814207b0b09e1a7e6cb20bc.png)
    
2.  > After selecting![](media/5cdab33a0a7ddd4ab5b2ca8cb04670be.png)，and click“Next”.

![](media/d70ecd0554cbdbd60997a2356b55dc0d.png)

3. > Click “Browse...”，select the location where Win32DiskImager is installed and click“Next”.

![](media/1cdc2638bc1e9fe214344429f5e97a13.png)

4.  > Click “Browse...”，select the location where Win32DiskImager is installed and click“Next”.
    
    ![](media/cc7949bb335b75000e77b18c85e4e07b.png)
    
5.  > Select![](media/99d088dd3f9e62d94fe8d56bd4638d1d.png)and click“Next”，and then click again“Install”.
    
    ![](media/c03510a9961a0e7307945dff10de3550.png)
    
    ![](media/0c9c0d647479ee984fc29c3cedc72c79.png)
    
    After a few seconds, the installation is complete, click "Finish".
    
    ![](media/1d75c6dd9ea4a2c437a2b655b713a1db.png)
    
    （5）Scan for IP address software tool---WNetWatcher Download Link：http://www.nirsoft.net/utils/wnetwatcher.zip
    

#### 1.3. Raspberry PI mirror system

Download link for the latest version：

[<span class="underline">https://www.raspberrypi.org/downloads/raspberry-pi-os/</span>](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

Download link for the old version：

  - > Raspbian：<span class="underline">https://downloads.raspberrypi.org/raspbian/images/</span>

  - > Raspbian full：<span class="underline">https://downloads.raspberrypi.org/raspbian\_full/images/</span>
    
  - > Raspbian lite：https://downloads.raspberrypi.org/raspbian\_lite/images/

We use the 2020.05.28 version in the tutorial and recommend you to use this version(Please download this version as shown in the picture below.)

<https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/>

![](media/857946c171dd1f5617a0cbbdd2608baf.png)

### 2. Install Raspberry Pi OS system on Raspberry Pi 4B:

#### **2.1. Interface the TFT memory card with a card reader, then plug the card reader into a computer’s USB port.**

#### **2.2. Use the SD Card Formatter to format a TFT memory card, as illustrated below：**

![](media/79d747e6f00f857a593b3327397cc44f.png)

![](media/cbc55902de71ce984d873ca2cb67fffa.png)

![](media/82031b5354cc4edeccf2bfa7465b7c6c.png)

#### **2.3. Burn system:**

（1）Use **Win32DiskImager** to burn the official **Raspberry Pi OS** mirror to the TFT memory card.

![](media/80d236cae8bdf63d80dc65048ffb52b3.png)

![](media/243d1ef34211eafe1a92b67fc0ee85a2.png)

![](media/ea854c476e9a8d4f82dd4a7c714cd5af.png)

（2）After the mirror system is burned, don’t pull out the card reader, use Notepad to create a file named **SSH**, delete**.txt**, and then copy it to the boot directory of the TFT card, so that you can open SSH login function, as shown in the following figure:

![](media/ffb73310322accd671da373bb2e71945.png)

（3）Pull out card reader.

#### **2.4. Log in system:**

（The following operations require raspberry to be on the same LOCAL area network as the PC）

##### （1）Preparation

Insert the burned TFT memory card into the Raspberry Pi, connect internet cable and plug in power. If you have a screen and a HDMI cable of Raspberry Pi, connect the screen, and you can see the Raspberry Pi OS startup screen. If you don't have an HDMI cable of Raspberry Pi, you can enter the desktop of Raspberry Pi via SSH remote login software---WinSCP and xrdp.

##### **（2）Remote login**

**Use WinSCP to log in using the default Raspberry Pi system name, default user name, default password.**

**Note that only a raspberry pi can be connected to a network.**

![](media/0a41d5c629ec98afbc31dc47ff5c18ec.png)

![](media/ff64e71b9e30df60d0b099dbc2532587.png)

##### **（3）View the ip address and mac address**

![](media/a4285a452978026c9e60c31d35974315.png)

Click to open terminal and input the password: raspberry, and tap“Enter”on keyboard.

![](media/a433a9ee584c821a702d0250937e2ba8.png)

![](media/7fb10d842cc7fd824a325d30fc3ecdc7.png)

After successful login, open the terminal, input **ip a** and tap“Enter”keyboard to view the ip address and mac address.

![](media/132e9ab754a0f63e38b3e4cfbc3679f2.png)

From the above figure, mac address of this Raspberry Pi is a6:32:17:61:9c, and ip address is 192.168.1.128(use ip address to finish
xrdp remote login).

Since mac address never changes, you could confirm ip via mac address when not sure which ip it is.

##### **（4）Fix the IP address of Raspberry Pi**

IP address is changeable, therefore, we need to make IP address fixed
for convenient use.

Follow the below steps:

Switch to root user

If without root user’s password

① Set root password

Input password in the terminal: sudo passwd root to set password.

② Switch to root user

su root

③ Fix the configuration file of IP address

Firstly change IP address of the following configuration file.

（\#New IP address:：address 192.168.1.99）

Copy the above new address to terminal and tap“**Enter**”keyboard.

Configuration File**:**

echo -e '

auto eth0

iface eth0 inet static

\#Change IP address

address 192.168.1.99

netmask 255.255.255.0

gateway 192.168.1.1

network 192.168.1.0

broadcast 192.168.1.255

dns-domain 119.29.29.29

dns-nameservers 119.29.29.29

metric 0

mtu 1492

'\>/etc/network/interfaces.d/eth0

Example operation diagram, as follows：

![](media/a68a4f59d4d364efa28b6680a2c48d43.png)

④ Reboot the system to activate the configuration file.

Input the restart command in the terminal: sudo reboot

You could log in via fixed IP afterwards.

⑤ Check IP and insure IP address fixed well.

![](media/b4313e2d78a4289705c658a1ebbc962b.png)

##### （5）Log in desktop on Raspberry Pi wirelessly

If we don't have an HDMI cable to connect to the display, can we wirelessly log in to the Raspberry Pi desktop from the Windows
desktop? Yes, there are many methods, VNC and Xrdp are commonly used to log in desktop of Raspberry Pi wirelessly.

Let’s take an example of Xrdp.

①Install Xrdp Service in the terminal

Installation commands:

Switch to root User: su root

Installation commands: apt-get install xrdp

Enter y and tap“**Enter**”keyboard..

As shown below:

![](media/aa59941ff4c1e582e8183c1dc3767fce.png)

Open the remote desktop connection on Windows

Press **WIN+R** on keyboard and enter mstsc.exe.

As shown below:

![](media/e5a66a3a1c998f8feb1c21c7a457ec4e.png)

Enter the IP address of the Raspberry Pi, as shown below. Click “Connect” and then click “Connect”again. 192.168.1.99 is the ip
address we use, you could change it into your IP address.

![](media/c41c66bea61b30019e02a74b483af700.png)

A prompt will appear and you can click“Yes”.

![](media/297813f1370ce5c158fac61511f61295.png)

Then enter the user name: pi ,and the default password: raspberry, as shown below:

![](media/251fddc1decc15d0b69f8a0c7467d5c1.png)

Click“OK”or tap“Enter”keyboard, you will view the desktop of Raspberry Pi OS, as shown below:

![](media/56bd5693edd484c4433dc438b58c6130.png)

Now, we finish the basic configuration of the Raspberry Pi OS system.

### 3. Preparation of C language control basic hardware:

[C](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/8.10.7.0/resultui/html/index.html#/javascript:;) [language](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/8.10.7.0/resultui/html/index.html#/javascript:;) is a programming language with a considerably fast running speed. There are numerous software and system core code written in it, such as Linux system. Notably, hardware MCU and embedded class are not exception. Thereby, it makes sense to learn the [C](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/8.10.7.0/resultui/html/index.html#/javascript:;) [language](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/8.10.7.0/resultui/html/index.html#/javascript:;) to control hardware.

#### (1)Description of basic raspberry pi accessories：

**Raspberry Pi 4B：**

Below are the raspberry pi pictures and model pictures supported by this learning kit. There are 40 pins.

| Raspberry Pi 4B         | Raspberry Pi 4B Model   |
| ----------------------- | ----------------------- |
| ![image-20231016090246338](media/image-20231016090246338.png) |![](media/67ac8e458430628f26cef46f04be3979.png)|

**Hardware Interfaces：**

![](media/d232a87d73f7426894a6cafed80521a0.png)

#### (2)Raspberry Pi +ESP32 mainboard + breadboard +USB cable, as shown below：

![](media/57cc1390c1a7a0bdd3525a17d65867d3.jpeg)

#### **(3)Copy Example Code Folder to Raspberry Pi：**

Place example code folder to the pi folder of Raspberry Pi. and Just copy and paste the **Arduino-Codes.zip** file (the default is **ZIP**
file) that we provided into user pi and unzip it, as shown below:

![](media/e7b577a013d27250449f6a6062f2a692.png)

![7d4668651b52a101834588ce80756ba9](./media/7d4668651b52a101834588ce80756ba9-1699599547292-1.png)

![83ed5ef4d005232ecd32aeec8e969173](./media/83ed5ef4d005232ecd32aeec8e969173-1699599956846-3.png)

![9e718971963a2a8542239e49f5fda29a](./media/9e718971963a2a8542239e49f5fda29a-1699600463947-5.png)

Double-click the **Arduino-Codes** file, as shown below.

![d768043901c5601e921983510d4bc460](./media/d768043901c5601e921983510d4bc460-1699600666996-7.png)

## Linux System（Raspberry Pi）：

### 1. Download and install Arduino IDE：

（1）First, click on Raspberry Pi's browser.

![](media/027fa8703101b0c296fbc82f9f246a36.png)

2.  Enter the Official Arduino website in your browser：[www.arduino.cc/en/software](http://www.arduino.cc/en/software) , as shown below:
    

![](media/64b964654fbdf403e42b61c753de120d.png)

![](media/e36e4d78ca3e5f57d51204d10be4b1a8.png)

（3）There are various versions of IDE for Arduino. Just download a version compatible with your system (install the lasted Arduino IDE) and click “Linux ARM 32 bits”.

![](media/673eacbf2dd436181621cbf2dd901cdd.png)

In general, you can click **JUST DOWNLOAD** to download, although if you like, you can choose a small sponsorship to help the great Arduino open source cause.

![](media/83d707e7d53788a08e63bab812298b09.png)

After a few seconds, the lasted Arduino IDE（Arduino 1.8.19 version）zip file can be directly downloaded.

(4) Click ![](media/673b0d8e5e8fc594f1914418da8d74a9.png), then find the **Downloads** file from the pi folder and click it. In the **Downloads** folder, you can see the
package“arduino-1.8.19-linuxarm.tar.xz”that you just downloaded. Then unzip the package“arduino-1.8.19-linuxarm.tar.xz”, after a while, the package is unzipped.

![](media/8bfa85ec821d531fc042e4e2aa4c40ce.png)

![](media/7721714f317a56214f4c14bfbfb92eeb.png)

![](media/0137b14e0053855856de0ff859ea1161.png)

![](media/2e144aae66a787d7c30945b24072b144.png)

（5）Click![](media/b479804e1f9ae2cdfaa0aad8495523d4.png)file and tap it，click“Execute”in the dialog that appears to install the Arduino IDE. Once installed, an Arduino software shortcut is generated in the desktop.

![](media/282a3e90f752066a10c69d75c58bc0be.png)

![](media/cc0f7b8a14fa5bdcb6560f51f6ffc917.png)

![](media/97bf23de0c9aa37db243d67d5e3f8670.png)

（6）Click ![](media/2ef5420fde334b93163b4a35e32e77dd.png)and click ![](media/cc7c9f3977d8da562ba2e98a6246c6b5.png) to open the Arduino IDE.

![](media/97f4118fc1f0d19aeb32a5af08812726.png)

![](media/f48690b0a3f56b9436ad4c56f0667af0.png)

### 2. Install the ESP32 on Arduino IDE：

Note: You need to download Arduino IDE 1.8.5 or advanced version to install the ESP32.

1)  > Click![](media/2ef5420fde334b93163b4a35e32e77dd.png) and ![](media/cc7c9f3977d8da562ba2e98a6246c6b5.png) to open the Arduino IDE.
    
    ![](media/6d61bd9f09f10763899e43a873b8bc75.png)



2)  Click**“File**”→**“Preferences”**，copy the website address <https://dl.espressif.com/dl/package_esp32_index.json> in
    the“**Additional Boards Manager URLs:**”and click“**OK**” to save the address.
    
    ![](media/834b8fc35034df92b21b36956fb1b300.png)

![](media/e509e8aece551e449ccb6ab6fffa0dc1.png)

3.  Click“**Tools**”→“**Board:**”,then click “**Boards Manager...**”to enter “**Boards Manager**” page . Enter“**esp32**”as follows and
    select the latest version to Install. The installation package is not large, click“**Install**”to start the installation.
    
    ![](media/ca9d80ba478d379d40afe119d60ec8cf.png)
    
    ![](media/b6d62e4c9cb8f530dc49b8ee92ecd76e.png)
    
    ![](media/1eaf35ef0b85b62a54733c2887bbced6.png)



4.  After a while, the ESP32 installation package is installed. Click “**Close**” to Close the page.
    
    ![](media/07d535a3532a58b15e79c9848ad8a019.png)

### 3. Arduino IDE Settings and toolbars:

（1）Click![](media/2ef5420fde334b93163b4a35e32e77dd.png) and ![](media/cc7c9f3977d8da562ba2e98a6246c6b5.png) to open the Arduino IDE.

![](media/8aca9b5378e794375f2c15d3b4e238ba.png)

（2）When downloading the code to the board, you must select the correct name of Arduino board that matches the board connected to the Raspberry Pi,click“**Tools**”→“**Board:**”. As shown below ;

(Note: we use the ESP32 board in this tutorial; therefore, we select ESP32 Arduino**)**

![](media/973eb76d6528c9464b0f03db2c679a64.png)

![](media/20172f3be362482efa80c49c2603b888.png)

Then select the correct COM port (After connecting the ESP32 mainboard to the Raspberry Pi via USB cable, you can see the corresponding COM port).

![](media/fab5efb1aeaae7e6864f1286934c89d7.png)

![](media/e341c279be4e2d1a53389e1124e5128d.png)

Before a code was uploaded to the ESP32 mainboard, we have to demonstrate the functionality of each symbol that appeared in the Arduino IDE toolbar.

![](media/d80f72747dd81a7c38022c057eaa6015.png)

A- Used to verify whether there is any compiling mistakes or not.

B- Used to upload the sketch to your Arduino board.

C- Used to create shortcut window of a new sketch.

D- Used to directly open an example sketch.

E- Used to save the sketch.

F- Used to send the serial data received from board to the serial monitor.



## Import the Arduino C library

Before starting the course, we also need to install the Arduino C library files required by the code in the course.

#### What are Libraries ?

[Libraries ](https://www.arduino.cc/en/Reference/Libraries)are a collection of code that make it easy for you to connect sensors,displays, modules, etc.

For example, the built-in LiquidCrystal library helps talk to LCD displays. There are hundreds of additional libraries available on the Internet for download.

The built-in libraries and some of these additional libraries are listed in the reference. (https://www.arduino.cc/en/Reference/Libraries)

Here we will introduce the most simple way to add libraries .

**Step 1:** Click ![](media/e927e911da6b964ab71f193c63403606.png)，tap“Downloads”file ![](media/83ad90890a4783af385a3dac7c0954a3.png)，and click“arduino-1.8.19”file![](media/df44a04c4d9dc93465a56e4ff7c9d184.png)，then find and click“libraries” file ![](media/630636db590e92c4969f89967124f96f.png)from the “arduino-1.8.19”file.

![](media/8fd90361aa115003241352cad2d9072d.png)

![](media/52a6147ae9a153e322672a52f96a4c6d.png)

![](media/438dd551f77795e04c4c532374dc13cc.png)

![](media/fcdfbb335828776c4b8d4a56f3833958.png)

![](media/e63db82531b8923e77969bf95662e446.png)

**Step 2 :** Copy and paste the Arduino C library ZIP file (the default is ZIP file) from the provided Arduino Libraries folder into the
libraries file opened in the first step（the route is：/home/pi/Downloads/arduino-1.8.19/libraries）.

Click on the link to download the Libraries file: [Download Libraries file](Arduino-Libraries.zip)

![7d4668651b52a101834588ce80756b1a9](./media/7d4668651b52a101834588ce80756b1a9.png)

![a843a93391975522f3c4d8ee897e65816](./media/a843a93391975522f3c4d8ee897e65816.png)

![](media/c7efc464d13c44c25f51339e655b2297.png)

> **Step 3:** Unzip the Arduino C package in the libraries folder（for example：right-click “ESP32Servo-0.8.0.zip”file![](media/46b12af0b61e04e540800708c3071214.png), select and tap “Extract Here”to unzip the “ESP32Servo-0.8.0.zip”file. Similarly, unzip the remaining library files in the same way.). So you can see all the decompressed Arduino C library files.

![](media/4bf511f1011dee54b6d55ede4b333547.png)





![](media/65303335cc527e9262fd3bb44f27128e.png)

![](media/6a70e117f09269b096a792959fb6b707.png)

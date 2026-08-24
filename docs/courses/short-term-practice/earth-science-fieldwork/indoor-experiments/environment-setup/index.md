**地球物理环境/软件/脚本配置**

下载anaconda

<img src="gfm-media/media/image1.png" style="width:5.75764in;height:2.80833in" />

进入网址，下面是账号密码（应该是属于内部资料所以密码作打码处理）

<img src="gfm-media/media/image2.png" style="width:3.16667in;height:1.125in" alt="/Users/b810/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/photoeditapp/20260822181314/temp.pngtemp" />

下载压缩包DenseArray……zip和XGBzip

**<span class="mark">matlab部分</span>**

<img src="gfm-media/media/image3.png" style="width:5.76597in;height:3.21736in" />

点击mlapp文件

<img src="gfm-media/media/image4.png" style="width:5.75556in;height:4.02083in" />

依次点击setuppaths，loadconfiguration，readSACdata,

【按钮简介】

一般按顺序点

SetupPaths-设置数据路径

↓

LoadConfiguration加载配置文件

↓

ReadSACData读取 SAC 地震波形数据

↓

Preprocessing预处理波形数据

↓

Deconvolution反褶积，计算接收函数

↓

Stacking RFs叠加接收函数

↓

Plot Single Trace画单条波形或单条接收函数

/ Plot Station Gather画台站集合图

/ Plot Event Gather画事件集合图

/ Plot Station–Event Map画台站—事件分布图

processing里面更改下拉框可以显示

<img src="gfm-media/media/image5.png" style="width:5.76389in;height:4.04653in" />

**<span class="mark">python部分</span>**

下载完anaconda检查一下

<img src="gfm-media/media/image6.png" style="width:4.84722in;height:0.45833in" />

有版本号的输出即为下载成功

把刚刚下载的文件夹拖进命令行，就会自动填充路径

<img src="gfm-media/media/image7.png" style="width:5.75972in;height:2.30625in" />

回车，进入该路径

mac的话输入ls查看文件夹内容；windows输入dir查看

<img src="gfm-media/media/image8.png" style="width:5.76736in;height:2.13333in" />

打开readme，可以看操作

<img src="gfm-media/media/image9.png" style="width:4.62569in;height:2.27917in" />

把文件中这句话“conda create --name xgboost_thickness python=3.10”

复制到命令行，回车执行

<img src="gfm-media/media/image10.png" style="width:5.33333in;height:3.43056in" />

执行过程中会出现询问是否继续“Proceed( \[y\] / n )?”

输入y并且回车，表示yes继续执行

<img src="gfm-media/media/image11.png" style="width:3.74792in;height:2.00486in" />

出现下面的表示环境已经配置完成

<img src="gfm-media/media/image12.png" style="width:4.58333in;height:2.43056in" />

用前面readme.md文件中的“conda activate xgboost_thickness”激活环境

<img src="gfm-media/media/image13.png" style="width:5.76181in;height:0.33333in" />

然后安装一些需要的库/包，用指令“pip install -r requirements.txt”

（tip：激活环境成功命令行前面是（xgboost_thickness）而不再是base）

<img src="gfm-media/media/image14.png" style="width:5.76181in;height:0.17778in" />

命令行中输入jupyter notebook如果没有可能是没有安装（下图自检了版本未输出说明还没安装）需要“pip install jupyter”或者“conda jupyter”

<img src="gfm-media/media/image15.png" style="width:5.76597in;height:1.50139in" />

安装好jupyter notebook后命令行再输入“jupyter notebook”，可以跳转到以下页面

<img src="gfm-media/media/image16.png" style="width:5.76806in;height:4.10417in" />

实习课主要用这两个

<img src="gfm-media/media/image17.png" style="width:5.76042in;height:2.32639in" />

点入某一个ipynb然后Run-Run All Cell运行

<img src="gfm-media/media/image18.png" style="width:5.7625in;height:3.1125in" />

运行完没报错说明环境都配置成功了，例如下图一直运行完了最后一个cell

<img src="gfm-media/media/image19.png" style="width:4.6875in;height:2.91736in" />

下次再要进入只需激活“conda activate xgboost_thickness”

进入“jupyter notebook”

<img src="gfm-media/media/image20.png" style="width:5.76389in;height:0.64167in" />

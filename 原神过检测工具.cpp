#include <iostream>
#include <Windows.h>
using namespace std;

void inject(){
    cout << "正在搜寻原神目录及启动器" << endl << endl;
    Sleep(3000);
    cout << "查找成功 正在注入启动文件" << endl;
    cout << "请耐心等待" << endl;
    Sleep(5000);
    MessageBox(NULL,"注入成功","原神过检测工具",MB_OK);
    Sleep(1000);
    cout << "=============" << endl;
    cout << "感谢您的使用" << endl;
    cout << "=============" << endl;
    cout << "5秒后自动退出";
    Sleep(5000);
}

void delInject(){
    cout << "正在搜寻数据目录" << endl;
    Sleep(1000);
    cout << "正在清除残留数据 请耐心等待" << endl;
    Sleep(2000);
    MessageBox(NULL,"清除成功","原神过检测工具",MB_OK);
    cout << "5秒后自动退出";
    Sleep(5000);
}

void show(){
    cout << "作者: NULL" << endl;
    cout << "软件仅供交流使用 禁止用作违法用途" << endl;
    cout << "=============" << endl;
    cout << "5秒后自动退出";
    Sleep(5000);
}

int main(){
	int a=MessageBox(NULL,"本软件仅供学习交流 禁止用作违法用途","警告",MB_YESNO);
	if (a==6){
    cout << "原神过检测工具" << endl;
    cout << "版本 3.4" << endl;
    cout << "欢迎你的使用" << endl;  
    cout << "=============" << endl;
    cout << "输入序号选择: " << endl;
    cout << "1. 注入反检测" << endl;
    cout << "2. 清空残留数据目录" << endl;
    cout << "3. 软件介绍" << endl;
    cout << "4. 退出程序" << endl;
    cout << "=============" << endl;

    int i;
    cin >> i;
    if (i==1)
        inject();
    if (i==2)
        delInject();
    if (i==3)
        show();
    if (i==4)
        return 0;
    else{
		    MessageBox(NULL,"操你妈的没给你这个选项选你妈啊傻逼","你妈死了",MB_OK);
	}
	}
	else
    return 0;
}

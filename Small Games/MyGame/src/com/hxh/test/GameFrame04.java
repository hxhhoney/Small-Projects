package com.hxh.test;

import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import com.hxh.test.GameFrame.PaintThread;

public class GameFrame04 extends MyFrame{

	private double x=100,y=100;
	private double degree=3.14/3;
	
	@Override
	public void paint(Graphics g) {//g is like a pencil.

		g.drawImage(img,(int)x,(int)y,20,20,null );//come with PaintThread
		
		x = 100+100*Math.cos(degree);
		y = 200+50*Math.sin(degree);
		
		degree += 0.1;
		

	}
	public static void main(String[] args){
		GameFrame04 gf=new GameFrame04();
		gf.launchFrame();
	}
}

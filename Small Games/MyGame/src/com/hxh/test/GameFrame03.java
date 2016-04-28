package com.hxh.test;
import java.awt.Color;
import java.awt.Font;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
/**
 * GameFrame Class
 * @author Cathy Huang
 * To test the movement of objects.
 */
public class GameFrame03 extends MyFrame{	
	private double x=100,y=100;
	private boolean left;
	@Override
	public void paint(Graphics g) {//g is like a pencil.
		
		
		g.drawImage(img,(int)x,(int)y,20,20,null );//come with PaintThread
		if(left)
			{x -= 10;}
		else
			{x+=10;}
		if(x>500-30)
			left=true;
		if(x<0)
			left=false;

	}
	/**
	 * Define a PaintThread Thread class, internal class
	 * @author DuckCathy
	 *
	 */

	public static void main(String[] args){
		GameFrame03 gf=new GameFrame03();
		gf.launchFrame();
	}
}

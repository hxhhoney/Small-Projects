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
 * Billiards GameFrame
 */
public class GameFrame02 extends MyFrame{

	private double x=100,y=100;
	private double degree=3.14/3;//[0,2pi]
	private double speed=10;
	@Override
	public void paint(Graphics g) {//g is like a pencil.
		
		
		g.drawImage(img,(int)x,(int)y,20,20,null );//come with PaintThread
		x += speed*Math.cos(degree);
		y += speed*Math.sin(degree);
		if(speed>0)
		{
			speed -= 0.2;
		}
		else
		{
			speed=0;
		}
		if(y<30||y>500-30){
			degree = -degree;
		}
		if(x<0||x>500-30){
			degree = Math.PI-degree;
		}
		
	}
	/**
	 * Define a PaintThread Thread class, internal class
	 * @author DuckCathy
	 *
	 */
	public static void main(String[] args){
		GameFrame02 gf=new GameFrame02();
		gf.launchFrame();
	}
}

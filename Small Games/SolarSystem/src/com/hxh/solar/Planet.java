package com.hxh.solar;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;

import com.hxh.util.GameUtil;

public class Planet extends Star{
	
	double longAxis;
	double shortAxis;
	double speed;
	double degree;
	Star center;
	
	
	public void draw(Graphics g){
		g.drawImage(img,(int)x,(int)y,15,15,null);
		//super.draw(g);	
		
		drawTrace(g);
		move();	
	}
	public void move()
	{
		x=center.x+50/2+longAxis*Math.cos(degree);//50 is the width of the image(not the real size) 
		y=center.y+50/2+shortAxis*Math.sin(degree);//if want to use the real size, use center.width
		degree +=speed;
	}
	
	public void drawTrace(Graphics g){
		double _x,_y,_width,_height;
		_width=longAxis*2;
		_height=shortAxis*2;
		_x=center.x+50/2-longAxis;
		_y=center.y+50/2-shortAxis;
		
		Color c=g.getColor();
		g.setColor(Color.blue);
		g.drawOval((int)_x,(int)_y,(int)_width,(int)_height);
		g.setColor(c);
		
	}
	
	
	public Planet(Image img,double x,double y){
		super(img,x,y);
	}
	

	public Planet(Star center, String imgpath, double longAxis, double shortAxis, double speed) {
		
		this.x=center.x+longAxis;//inherit from Star
		this.y=center.y;
		this.img=GameUtil.getImage(imgpath);
		
		this.longAxis = longAxis;
		this.shortAxis = shortAxis;
		this.speed = speed;
		this.center = center;
		
		this.width= img.getWidth(null);
		this.depth= img.getHeight(null);
	}
	public Planet(String imgpath,double x,double y){
		super(imgpath,x,y);
	}
	

}

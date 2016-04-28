package com.hxh.solar;

import java.awt.Graphics;
import java.awt.Image;

import com.hxh.util.GameUtil;

public class Star {
	Image img;
	double x,y;
	int width;
	int depth;
	
	
	
	public void draw(Graphics g){
		g.drawImage(img,(int) x,(int) y,50,50,null);	
	}
	
	public Star(){}
	public Star(Image img){
		this.img=img;
		this.width= img.getWidth(null);
		this.depth= img.getHeight(null);
	}
	public Star(Image img,double x, double y){
		this(img);
		this.x=x;
		this.y=y;

		
	}
	public Star(String imgpath,double x,double y){
		this(GameUtil.getImage(imgpath),x,y);
		//this.img=GameUtil.getImage(imgpath);
		//this.x=x;
		//this.y=y;
		
	}
}

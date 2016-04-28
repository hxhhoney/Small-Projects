package com.hxh.solar;

import java.awt.Graphics;
import java.awt.Image;

import com.hxh.util.Constant;
import com.hxh.util.GameUtil;
import com.hxh.util.MyFrame;

/**
 * Main Window for SolarSystem
 * @author DuckCathy
 *
 */

public class SolarFrame extends MyFrame{
	Image bg=GameUtil.getImage("solarimages/bg.jpg");
	Star sun=new Star("solarimages/sun.jpg",Constant.GAME_WIDTH/2,Constant.GAME_HEIGHT/2);
	Planet mercury=new Planet(sun, "solarimages/mercury.jpg", 70, 50, 0.012);
	Planet venus=new Planet(sun, "solarimages/venus.jpg", 100, 80, 0.031);
	Planet earth=new Planet(sun, "solarimages/earth.jpg", 150, 100, 0.05);
	Planet moon=new Planet(earth, "solarimages/moon.jpg", 30, 20, 15);
	
	Planet mars= new Planet(sun,"solarimages/mars.jpg",200,130,0.094);
	Planet jupiter= new Planet(sun,"solarimages/jupiter.jpg",230,150,0.593);
	Planet saturn= new Planet(sun,"solarimages/saturn.jpg",250,170,1.473);
	Planet uranus= new Planet(sun,"solarimages/uranus.jpg",300,270,4.205);
	Planet napturn= new Planet(sun,"solarimages/naptune.jpg",400,390,8.241);
	
	
			
	public void paint(Graphics g){
		g.drawImage(bg, 0, 0, null);
		sun.draw(g);
		mercury.draw(g);
		venus.draw(g);
		earth.draw(g);
		mars.draw(g);
		moon.draw(g);
		jupiter.draw(g);
		saturn.draw(g);
		uranus.draw(g);
	
	}
	public static void main(String[] args){
		new SolarFrame().launchFrame();
	}

}

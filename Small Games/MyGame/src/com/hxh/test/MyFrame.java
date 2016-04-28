package com.hxh.test;

import java.awt.Frame;
import java.awt.Image;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import com.hxh.test.GameFrame.PaintThread;

public class MyFrame extends Frame{
	
	/**
	 * launchImage
	 */
	Image img = GameUtil.getImage("images/IMG_0823.JPG");	
	public void launchFrame(){
		setSize(Constant.GAME_WIDTH,Constant.GAME_HEIGHT);
		setLocation(100,100);
		setVisible(true);//let the window be visible
		
		new PaintThread().start();//launch PaintThread;//
		
		addWindowListener(new WindowAdapter(){//to close window
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}	
		});
	}
		class PaintThread extends Thread{
			public void run(){
				while(true){//Dead loop, draw the whole platform until exit the game
					
					repaint();//exist in GameFrame
					
					try {
						Thread.sleep(40);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}// ls=1000ms
					
					
				}
			}
		}
}

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
 *
 */
public class GameFrame extends Frame{
	/**
	 * launchImage
	 */
	Image img = GameUtil.getImage("images/IMG_0823.JPG");
	
	/**
	 * launchFrame
	 */
	public void launchFrame(){
		setSize(500,500);
		setLocation(100,100);
		setVisible(true);//let the window be visible
		
		new PaintThread().start();//launch PaintThread;
		
		addWindowListener(new WindowAdapter(){//to close window
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}	
		});
	}
		private double x=100,y=100;
	@Override
	public void paint(Graphics g) {//g is like a pencil.
		System.out.println("Paint!");
		g.drawLine(100, 100, 200, 200);
		g.drawRect(100, 100, 200, 200);
		g.drawOval(100,100, 200, 200);
		
		//g.drawImage(img, 400,400,20,20,null);
		g.drawImage(img,(int)x,(int)y,20,20,null );//come with PaintThread
		x += 3;//move the image
		y += 3;
		
		
		Font f=new Font("ITALIC",50,50);
		g.setFont(f);
	
		g.drawString("My name is Cathy", 200, 200);
		g.fillRect(100,100,20,20);
		Color c=g.getColor();
		g.setColor(Color.BLUE);
		g.fillOval(300, 300, 20, 20);
		g.setColor(c);//to let the color of pencil back to the original.
	}
	/**
	 * Define a PaintThread Thread class, internal class
	 * @author DuckCathy
	 *
	 */
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
	public static void main(String[] args){
		GameFrame gf=new GameFrame();
		gf.launchFrame();
	}
}

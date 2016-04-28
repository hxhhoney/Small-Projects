package com.hxh.test;

import java.awt.Image;
import java.awt.Toolkit;
import java.net.URL;


/**
 * GameUtil class, for tools.
 * @author DuckCathy
 *Methods are always static
 */

public class GameUtil {
	public static Image getImage(String path){//Image is a class
		URL u=GameUtil.class.getClassLoader().getResource(path);
		
		return Toolkit.getDefaultToolkit().getImage(u);
	}
}

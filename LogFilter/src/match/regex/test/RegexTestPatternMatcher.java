package match.regex.test;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class RegexTestPatternMatcher {
	public static String pattern2;
	public static void readProperties() throws IOException{
		  Properties pro=new Properties();
		  FileInputStream in = new FileInputStream("parameters.properties");
		  pro.load(in);
		  //getting values from property file
		  pattern2=pro.getProperty("profileId");
		  
		  
	}
	public static void stringReceiver( String line ) throws IOException{

	      // String to be scanned to find the pattern.
	      //String line = "[2016-06 16][DEBUG] server https://api2.iheart.com/api/v1/liveRadio/206706278/849/thumbsUpTrack";
	      //System.out.println(line);

		  String pattern1 = "(.*)http(.*)"; 
	      String pattern3="\\[DEBUG](.*)";
	      
	     
	     
	      //System.out.println(regexChecker(pattern1,line));
	      if(regexChecker(pattern2,line)!=null&&regexChecker(pattern3,line)!=null&&regexChecker(pattern1,line)!=null)
	      {
	    	  System.out.println(line);
	    	  OutputManager.outfile(line); 
	      } 
	   }
	
	public static String regexChecker(String pattern, String line)
	{
		Pattern checkPattern=Pattern.compile(pattern);
		Matcher checkMatcher=checkPattern.matcher(line);
		while(checkMatcher.find()){
			if(checkMatcher.group().length()!=0){
				//System.out.println(checkMatcher.group().trim());
				return checkMatcher.group().trim();
			}	
		}
		return null;
	}

}

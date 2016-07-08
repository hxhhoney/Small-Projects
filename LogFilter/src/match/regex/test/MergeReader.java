package match.regex.test;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class MergeReader {
	public Scanner reader;
	public String current;
	public String next;

	public  void setupReader(String name) throws FileNotFoundException{
		//System.out.println(name);
		String filename=name;
		File file=new File(filename);
	    reader=new Scanner(file);
	    if(reader.hasNextLine())
	    {
	    	current=reader.nextLine();
	    	if(reader.hasNextLine())
	    	{
	    		next=reader.nextLine();
	    		if(reader.hasNextLine())
	    		{
	    			next=reader.nextLine();
	    			
	    		}	
	    		
	    	}
	    }
	    //System.out.println(current);
	    //System.out.println(next);
	    
	}
	public  void readNextLine(){
		current=next;
		if(reader.hasNextLine())
		{
			next=reader.nextLine();
			if(reader.hasNextLine())
				{
				next=reader.nextLine();
				}
		}
		else
		{
			reader.close();
		}
		//System.out.println("Current:"+current);
		//System.out.println("Next:"+next);
		
	}	

}

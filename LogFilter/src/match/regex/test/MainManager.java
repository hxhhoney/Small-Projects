package match.regex.test;

import java.io.File;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;

public class MainManager {
	 public static int filesize(String filename)
	    {
	    	return new File(filename).listFiles().length-1;
	    }
		
	 public static void merge() throws IOException{
			Outcomer.setupoutfile();
	    	int inputsize=filesize("input");
			//System.out.println(inputsize);
			
			MergeReader[] m=new MergeReader[inputsize+1];
			Comparator<MergeReader> comparator = new Comparer();
			PriorityQueue<MergeReader> heap=new PriorityQueue<MergeReader>(inputsize, comparator);
				
			for(int i=1;i<=inputsize;i++)
			{
				m[i] = new MergeReader();
				m[i].setupReader("input/output"+i+".txt");	
				m[i].readNextLine();
				heap.add(m[i]);
			}
			//System.out.println(heap.peek().current);
			
			while(heap.size()!=0)
			{
				MergeReader top=heap.peek();
				//System.out.println(top.current);
				Outcomer.outfile(top.current);
				heap.poll();
				if(top.current!=top.next)
				{
					top.readNextLine();
					heap.add(top);
				}
			}
			}
}

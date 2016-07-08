package match.regex.test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Comparer implements Comparator<MergeReader>{
	
	@Override
	public int compare(MergeReader o, MergeReader o2) {
		// TODO Auto-generated method stub
		String s=o.current;
		String s2=o2.current;
		String year=s.substring(1, 5);
		String month=s.substring(6, 8);
		String day=s.substring(9, 11);
		String hour=s.substring(12, 14);
		String bigtime=year+month+day+hour;
		
		int big=Integer.parseInt(bigtime);
		
		String minu=s.substring(15,17);
		String sec=s.substring(18, 20);
		String milisec=s.substring(21, 24);
		String minitime=minu+sec+milisec;
		
		int small=Integer.parseInt(minitime);
		
		String year2=s2.substring(1, 5);
		String month2=s2.substring(6, 8);
		String day2=s2.substring(9, 11);
		String hour2=s2.substring(12, 14);
		String bigtime2=year2+month2+day2+hour2;
		
		int big2=Integer.parseInt(bigtime2);
		
		String minu2=s2.substring(15,17);
		String sec2=s2.substring(18, 20);
		String milisec2=s2.substring(21, 24);
		String minitime2=minu2+sec2+milisec2;
		
		int small2=Integer.parseInt(minitime2);
		
		if(big<big2)
			return -1;
		else if(big==big2)
		{
			if(small<=small2)
				return -1;
		}
		return 1;
		
	}
	
}

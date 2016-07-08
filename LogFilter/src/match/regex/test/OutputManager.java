package match.regex.test;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class OutputManager {
	static BufferedWriter output;
	public static void setupoutfile(int j) throws IOException{
		File outfile=new File("input/output"+j+".txt");
		output =new BufferedWriter(new FileWriter(outfile));
	}
	public static void outfile(String s) throws IOException{
		output.newLine();
		output.newLine();
		output.write(s);
		output.flush();

	}

}

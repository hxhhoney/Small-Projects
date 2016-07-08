package match.regex.test;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
public class Outcomer {
		static BufferedWriter output;
		
		public static void setupoutfile() throws IOException{
			File outfile=new File("finaloutput.txt");
			output =new BufferedWriter(new FileWriter(outfile));
		}
		public static void outfile(String s) throws IOException{
			output.newLine();
			output.newLine();
			output.write(s);
			output.flush();
		}

}

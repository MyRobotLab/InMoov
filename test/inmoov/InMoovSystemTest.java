package inmoov;

import java.io.File;
import java.io.IOException;

import org.junit.Test;
import org.junit.Ignore;
import org.myrobotlab.service.Python;
import org.myrobotlab.service.Runtime;

/**
 * This is a simple junit test that can be used to load the InMoov default scripts. 
 * To use this unit test, you must checkout the myrobotlab project and import it into this project.
 * For eclipse:
 * In the myrobotlab project, open up the "Java Build Path" and then choose the "Order and Export" tab. 
 * On the "Order and Export" tab ensure that the maven dependencies are selected to be exported.
 * 
 * The InMoov project needs to be setup with a java nature to support running java code.  
 * Update the java build path to reference the myrobotlab project, this will bring in all of the java dependencies.
 * 
 * At that point, you can run the script below and it will launch the default InMoov scripts.
 * Make sure to remove or comment out the @Ignore annotation at the top of the class to run it.
 * 
 * TODO: the self extracted resources need to be fixed so that the webgui will launch.
 * 
 */
@Ignore
public class InMoovSystemTest {

	@Test
	public void testInMoov() throws IOException {
		// TODO: launch the inmoov!
	    Python python = (Python)Runtime.start("python", "Python");
	    String inMoovScript = "./InMoov/InMoov.py";
	    File f = new File(inMoovScript);
	    System.out.println(f.getAbsolutePath());
	    python.execFile(inMoovScript);
	    System.out.println("Press the any key.");
	    System.in.read();
	    
	}
}

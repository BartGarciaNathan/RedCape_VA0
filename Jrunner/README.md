RedCape_VA0
===========
Intro to RedCape


Jrunner
==========

This is a working version of Jrunner for the BeagleBone Black with the RedCape VA0. It should work with the BeagleBone White as well but it had not been tested yet. 

One of the possibilities for configuring the Altera Cyclone V FPGA in the RedCape, is to use Jrunner. Jrunner is  a C program that runs in the BeagleBone processor and uses four lines to communicate with the JTAG interface in the Cyclone V.  Jrunner is a software designed  by Altera, and the original source code can be find at : https://www.altera.com/download/legacy/jrunner/dnl-jrunner.html
This version is based on that code but modified to work in the BeagleBone Black and to use the correct pin assignments for the Cyclone V in the RedCape. The source code used for this can be obtained in the /src directory of this repository. 

How to use Jrunner 

Step 1 – Obtain Configuring files
Jrunner allows the user to configure the FPGA since the embedded processor, but to do this its necessary to have a working project configuration for the FPGA. The project must be saved as an Raw Binary File(RBF) file to be sent to the FPGA. To obtain the RBF file its possible to use Altera Quartus. From the Quartus main window, with the selected project open, follow the next steps:

File → Convert programming Files 
In the Convert programming File window, select the next
Programming file type : Raw Binary File (RBF)
Mode : 1 bit passive serial

Enter the desired output file name. In desired Files to convert, follow the next steps :
Select : SOF DATA  and Add File ( Here its necessary to select the .sof file of the compiled project, its usually in the /output_files directory) 
Then just click Generate, the RBF file should be ready.

Now we need to obtain an .cdf file that will tell Jrunner some information about the FPGA and the RBF. The easiest way to do this is to open the “cog_profiler.cdf” file and modify the name file accordingly. The file contains the next text :
```

/* Quartus II Version 9.1 Build 350 03/24/2010 Service Pack 2 SJ Full Version */

JedecChain;

	FileRevision(JESD32A);

	DefaultMfr(6E);



	P ActionCode(Cfg)

		Device PartName(5CGXFC3B6U19) Path("") File("file.rbf") MfrSpec(OpMask(1));



ChainEnd;



AlteraBegin;

	ChainType(JTAG);

AlteraEnd;
```

It is necessary to modify the File value, so change “file.rbf” for the name given to the RBF in the Altera Convert Programming File. Its maybe simpler to have a .cdf file for each RBF file, so its a good idea to save the .cdf file with the same name as the .rbf file to which is pointing. 

NOTE : The RBF file must have its name all in caps, both in the directory and in the reference to it in the .cdf file.

Once all this files are ready,  its necessary to put all of them (.rbf, .cdf , jrunner) together in the same directory.

Step 2 – Setting the DipSwitch

Set the correct mode in the DipSwitch. The connection of the BeagleBone processor to the FPGA for the JTAG configuration is controlled by a 4-bit bidirectional translator, so it needed to activate the desired mode. For this, the bit 4 of the DipSwitch (SW1) in the RedCape is used. If the bit is OFF then the communication is possible. So ensure to set this bit to  OFF before using the Jrunner. If the bit is set to ON then the jrunner will show a “ JTAG chain broken! “ Error.

Step 3 -  Calling jrunner from command line. 

After obtaining the files from the Github Repository, its necessary to give the right permissions to the jrunner file. To do so :

	$chmod +x jrunner


With the right permissions now we can execute the file. So the usage for configuring the Cyclone V FPGA is :

	$./jrunner redcapea0_demo.cdf 

To configure the demo project. To use it for another project just type the name of the .cdf file needed.

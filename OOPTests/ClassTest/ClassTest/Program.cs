using System;

namespace ClassTest
{
	public class test
	{
		public int i1;
		public int i2;

		public test()
		{

		}
	}

	class MainClass
	{
		public static void Main (string[] args)
		{
			test ins1 = new test ();
			ins1.i1 = 1;
			ins1.i2 = 2;

			//basically, this is the equation of pointers. (passing references)
			test ins2 = ins1;

			Console.WriteLine ("Instance 2: " + ins2.i1 + " " + ins2.i2);

			ins2.i2 = 4;
			ins1.i1 = 3;

			Console.WriteLine ("Instance 2: " + ins2.i1 + " " + ins2.i2);
			Console.WriteLine ("Instance 1: " + ins1.i1 + " " + ins1.i2);
		}
	}
}

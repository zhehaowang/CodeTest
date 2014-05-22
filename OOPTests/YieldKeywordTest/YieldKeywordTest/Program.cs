using System;
using System.Collections;
using System.Collections.Generic;

using System.Threading;

namespace YieldKeywordTest
{
	class YieldKeywordTest
	{
		// this is the sample from MSDN, still, I don't quite see the point of yield aside from being a syntactical sugar?
		static void Main()
		{
			// Display powers of 2 up to the exponent of 8: 
			foreach (int i in Power(2, 8))
			{
				Console.Write("{0}\n", i);
			}
			Console.WriteLine ("It does not have anything to do with sync or async.");
		}

		public static IEnumerable<int> Power(int number, int exponent)
		{
			int result = 1;

			for (int i = 0; i < exponent; i++)
			{
				result = result * number;
				yield return result;
				Console.WriteLine ("lines after yield result is still executed");
				Thread.Sleep (500);
			}
		}
	}
}

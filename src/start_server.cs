using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace form_with_http
{
    internal class start_server
    {
        public static void OpenApplication()
        {
            using (Process compiler = new Process())
            {
                //compiler.StartInfo.FileName = "server.exe";
                //compiler.StartInfo.UseShellExecute = false;
                //compiler.StartInfo.RedirectStandardOutput = true;
                //compiler.Start();

                //Console.WriteLine(compiler.StandardOutput.ReadToEnd());

                //compiler.WaitForExit();

                var p = new Process();
                p.StartInfo = new ProcessStartInfo(@"C:\Users\Mvine\source\repos\form with http\form with http\bin\Debug\net8.0-windows\myscript.bat")
                {
                    UseShellExecute = true
                };
                p.Start();
            }
        }
    }
}

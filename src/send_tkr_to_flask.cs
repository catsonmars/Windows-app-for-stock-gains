//Console.WriteLine("Hello, World!");
/*dependencies
system.net.http
 */
using form_with_http;
using Newtonsoft.Json;
using System;
using System.Text;
using System.Dynamic;
using System.Net;
using System.Net.Http;
//this gets information from python but I want it to SEND information!
namespace server
{
    static class Send_Post
    {
        public static string Submit(string usr_input)
        {
            using (var client = new HttpClient())
            {
                //var endpoint = new Uri("http://127.0.0.1:5000/feminism");
                var endpoint = new Uri("http://127.0.0.1:5000/pp");
                var newPost = new Post()
                {
                    ticker = usr_input
                };
                var newPostJson = JsonConvert.SerializeObject(newPost);
                var payload = new StringContent(newPostJson, Encoding.UTF8, "application/json");
                //while (true) 
                {
                    var result = client.PostAsync(endpoint, payload).Result.Content.ReadAsStringAsync().Result;
                    return result;
                }

                //var result = client.GetAsync(endpoint).Result.Content.ReadAsStringAsync().Result;
                //Console.Write(result);

            }
            
        }
    }
}
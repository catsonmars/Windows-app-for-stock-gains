using server;

namespace form_with_http
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var response = Send_Post.Submit(textBox1.Text);
            //MessageBox.Show("You entered in " + textBox1.Text); //debug
            MessageBox.Show(response);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}

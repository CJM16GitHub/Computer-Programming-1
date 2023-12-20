import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(587, 177)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(80, 69)
		self._button1.TabIndex = 0
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Fuchsia
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(759, 252)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(80, 69)
		self._button2.TabIndex = 1
		self._button2.Text = "//"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(628, 327)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(166, 59)
		self._button3.TabIndex = 2
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.Red
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(628, 392)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(166, 59)
		self._button4.TabIndex = 3
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(203, 166)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(211, 49)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(203, 476)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(211, 49)
		self._textBox2.TabIndex = 5
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Blue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 166)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(185, 49)
		self._label1.TabIndex = 6
		self._label1.Text = "Number 1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Blue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 327)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(185, 49)
		self._label2.TabIndex = 7
		self._label2.Text = "Operation"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Blue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 476)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(185, 49)
		self._label3.TabIndex = 8
		self._label3.Text = "Number 2"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Blue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 625)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(185, 49)
		self._label4.TabIndex = 9
		self._label4.Text = "Result"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Red
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(203, 327)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(211, 49)
		self._label5.TabIndex = 10
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Red
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(203, 625)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(211, 49)
		self._label6.TabIndex = 11
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Red
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(587, 112)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(252, 59)
		self._button5.TabIndex = 12
		self._button5.Text = "MOD"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.Yellow
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(673, 177)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(80, 69)
		self._button6.TabIndex = 13
		self._button6.Text = "-"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.Lime
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(759, 177)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(80, 69)
		self._button7.TabIndex = 14
		self._button7.Text = "*"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.Blue
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(587, 252)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(80, 69)
		self._button8.TabIndex = 15
		self._button8.Text = "^"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(673, 252)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(80, 69)
		self._button9.TabIndex = 16
		self._button9.Text = "/"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(901, 749)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg140"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		dblResult = 0.0
		self._label5.Text = "+"
		dblResult = float(self._textBox1.Text) + float(self._textBox2.Text)
		self._label6.Text = str(dblResult)

	def Button2Click(self, sender, e):
		intResult = 0
		self._label5.Text = "//"
		intResult = int(self._textBox1.Text) // int(self._textBox2.Text)
		self._label6.Text = str(intResult)

	def Button3Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._label5.Text = ""
		self._label6.Text = ""

	def Button4Click(self, sender, e):
		Application.Exit()

	def Button5Click(self, sender, e):
		intResult = 0
		self._label5.Text = "%"
		intResult = int(self._textBox1.Text) % int(self._textBox2.Text)
		self._label6.Text = str(intResult)

	def Button6Click(self, sender, e):
		dblResult = 0.0
		self._label5.Text = "-"
		dblResult = float(self._textBox1.Text) - float(self._textBox2.Text)
		self._label6.Text = str(dblResult)

	def Button7Click(self, sender, e):
		dblResult = 0.0
		self._label5.Text = "*"
		dblResult = float(self._textBox1.Text) * float(self._textBox2.Text)
		self._label6.Text = str(dblResult)

	def Button8Click(self, sender, e):
		intResult = 0
		self._label5.Text = "^"
		intResult = int(self._textBox1.Text) ^ int(self._textBox2.Text)
		self._label6.Text = str(intResult)

	def Button9Click(self, sender, e):
		intResult = 0
		self._label5.Text = "/"
		intResult = int(self._textBox1.Text) / int(self._textBox2.Text)
		self._label6.Text = str(intResult)
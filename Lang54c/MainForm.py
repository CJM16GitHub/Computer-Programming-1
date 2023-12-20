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
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 613)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(206, 117)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(308, 613)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(206, 117)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(628, 613)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(206, 117)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.HotTrack
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 111)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(502, 66)
		self._label1.TabIndex = 3
		self._label1.Text = "Radius:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Click += self.Label1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(520, 128)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(314, 49)
		self._textBox1.TabIndex = 5
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.HotTrack
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 309)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(502, 66)
		self._label2.TabIndex = 6
		self._label2.Text = "Circumference:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.HotTrack
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 507)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(502, 66)
		self._label3.TabIndex = 7
		self._label3.Text = "Area:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(520, 309)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(314, 66)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(520, 507)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(314, 66)
		self._label5.TabIndex = 9
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label5.Click += self.Label5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(846, 742)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Radius = 3.14159
		Circumference = 2
		
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label1.Text = "Radius: "
		self._label2.Text = "Circumference: "
		self._label3.Text = "Area: "
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass
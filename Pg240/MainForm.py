import math
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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 650)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(221, 88)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(337, 650)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(221, 88)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(668, 650)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(221, 88)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Blue
		self._label1.Location = System.Drawing.Point(12, 57)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(369, 52)
		self._label1.TabIndex = 3
		self._label1.Text = "Sales For The Month"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Blue
		self._label2.Location = System.Drawing.Point(12, 163)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(427, 52)
		self._label2.TabIndex = 4
		self._label2.Text = "Advanced Pay Awarded"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Blue
		self._label3.Location = System.Drawing.Point(12, 265)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(312, 52)
		self._label3.TabIndex = 5
		self._label3.Text = "Commission Rate"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Blue
		self._label4.Location = System.Drawing.Point(12, 365)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(230, 52)
		self._label4.TabIndex = 6
		self._label4.Text = "Commission"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Blue
		self._label5.Location = System.Drawing.Point(12, 469)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(153, 52)
		self._label5.TabIndex = 7
		self._label5.Text = "Net Pay"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Blue
		self._label6.Location = System.Drawing.Point(445, 265)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(444, 52)
		self._label6.TabIndex = 8
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Blue
		self._label7.Location = System.Drawing.Point(445, 365)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(444, 52)
		self._label7.TabIndex = 9
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Blue
		self._label8.Location = System.Drawing.Point(445, 469)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(444, 52)
		self._label8.TabIndex = 10
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(445, 57)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(444, 49)
		self._textBox1.TabIndex = 11
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(445, 166)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(444, 49)
		self._textBox2.TabIndex = 12
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Red
		self.ClientSize = System.Drawing.Size(901, 750)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Pg240"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		decSalesAmount = 0.0
		decAdvancedPayAmount = 0.0
		decCommissionRate = 0.0
		decCommissionAmount = 0.0
		decNetPay = 0.0
		
		if decSalesAmount < 10000:
			decCommissionRate = 0.05
		elif decSalesAmount >= 10000 and decSalesAmount < 15000:
			decCommissionRate = 0.1
		elif decSalesAmount >= 15000 and decSalesAmount < 18000:
			decCommissionRate = 0.12
		elif decSalesAmount >= 18000 and decSalesAmount < 22000:
			decCommissionRate = 0.14
		elif decSalesAmount >= 22000:
			decCommissionRate = 0.15
			
		decCommissionAmount = decSalesAmount * decCommissionRate
		decNet = decCommissionAmount - decAdvancePayAmount
		
		self._label6.Text = str(round(decCommissionRate, 2))
		self._label7.Text = str(round(decCommissionAmount, 2))
		self._label8.Text = str(round(decNetPay, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label6.Text.Clear()
		self._label7.Text.Clear()
		self._label8.Text.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()
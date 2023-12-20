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
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 660)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(218, 79)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(341, 660)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(218, 79)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(676, 660)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(218, 79)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.Blue
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(236, 141)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(225, 174)
		self._groupBox1.TabIndex = 3
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Type Of Membership"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.Blue
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.Location = System.Drawing.Point(467, 141)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(225, 174)
		self._groupBox2.TabIndex = 4
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Options"
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.Blue
		self._groupBox3.Controls.Add(self._label1)
		self._groupBox3.Controls.Add(self._textBox1)
		self._groupBox3.Location = System.Drawing.Point(236, 321)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(225, 174)
		self._groupBox3.TabIndex = 4
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Membership Length"
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.Color.Blue
		self._groupBox4.Controls.Add(self._label5)
		self._groupBox4.Controls.Add(self._label4)
		self._groupBox4.Controls.Add(self._label3)
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.Location = System.Drawing.Point(467, 321)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(225, 174)
		self._groupBox4.TabIndex = 4
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Membership Fees"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(6, 110)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(213, 49)
		self._textBox1.TabIndex = 5
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(213, 32)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Standard Adult"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 57)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(213, 32)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child (12 or Under)"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 95)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(213, 32)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(6, 133)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(213, 32)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior Citizen"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(6, 19)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(213, 32)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Yoga"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(6, 57)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(213, 32)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Karate"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(6, 95)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(213, 32)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Blue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 32)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(213, 75)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter The Number Of Months"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 32)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(132, 32)
		self._label2.TabIndex = 0
		self._label2.Text = "Monthly Fee"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 75)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(132, 32)
		self._label3.TabIndex = 1
		self._label3.Text = "Total"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(144, 32)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(75, 32)
		self._label4.TabIndex = 2
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(144, 75)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(75, 32)
		self._label5.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Red
		self.ClientSize = System.Drawing.Size(906, 751)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg250"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		decBaseFee = 0.0
		decDiscount = 0.0
		decTotalFee = 0.0
		intMonths = 0
		
		try:
			intMonths = int(self._textBox1.Text)
		except:
			MessageBox.Show("Months must be a valid integer", "Input Error")
			return
		
		if intMonths < 1 or intMonths > 24:
			MessageBox.Show("Months must be a valid integer", "Input Error")
			return
		
		if self._radioButton1.Checked == True:
			decBaseFee = 40
		elif self._radioButton2.Checked == True:
			decBaseFee = 20
		elif self._radioButton3.Checked == True:
			decBaseFee = 25
		elif self._radioButton4.Checked == True:
			decBaseFee = 30
			
		if self._checkBox1.Checked == True:
			decBaseFee += 10
		if self._checkBox2.Checked == True:
			decBaseFee += 30
		if self._checkBox3.Checked == True:
			decBaseFee += 50
		
		if intMonths <= 3:
			decDiscount = 0.0
		elif intMonths >= 4 and intMonths <= 6:
			decDiscount = decBaseFee * self.decDiscount4to6
		elif intMonths >= 7 and intMonths <= 9:
			decDiscount = decBaseFee * self.decDiscount7to9
		elif intMonths >= 10:
			decDiscount = decBaseFee * self.decDiscount10orMore
		
		decBaseFee -= decDiscount
		decTotal.TextFee = decBaseFee * intMonths
		
		self._label4.Text = str(round(decBaseFee, 2))
		self._label5.Text = str(round(decTotalFee, 2))

	def Button2Click(self, sender, e):
		self._radioButton1.Checked = True
		self._checkBox1.Checked = False
		self._checkBox2.Checked = False
		self._checkBox3.Checked = False
		self._textBox1.Clear()
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
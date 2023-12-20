require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(12, 618)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(187, 116)
		@button1.TabIndex = 0
		@button1.Text = "Canculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(324, 618)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(187, 116)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(644, 618)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(187, 116)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(260, 55)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(324, 47)
		@textBox1.TabIndex = 3
		@textBox1.TextChanged { |sender, e| self.TextBox1TextChanged(sender, e) }
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(260, 215)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(324, 47)
		@textBox2.TabIndex = 4
		@textBox2.TextChanged { |sender, e| self.TextBox2TextChanged(sender, e) }
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(260, 361)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(324, 47)
		@textBox3.TabIndex = 7
		# 
		# textBox4
		# 
		@textBox4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(260, 505)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(324, 47)
		@textBox4.TabIndex = 8
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.HotTrack
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(12, 53)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(210, 48)
		@label3.TabIndex = 9
		@label3.Text = "Average:"
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.HotTrack
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 503)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(210, 48)
		@label4.TabIndex = 10
		@label4.Text = "Sum:"
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label4.Click { |sender, e| self.Label4Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.Desktop
		self.ClientSize = System::Drawing::Size.new(843, 746)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Lang54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		num1 = int(@textBox1.Text)
		num2 = int(@textBox2.Text)
		num3 = int(@textBox3.Text)
		num4 = int(@textBox4.Text)
		sum = num1 + num2 + num3 + num4
		average = sum / 4.0
		@label3.Text = "Average: " + str(average)
		@label4.Text = "Sum: " + str(sum)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
		@Label3.Text = ""
		@Label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def TextBox1TextChanged(sender, e)
		
	end

	def TextBox2TextChanged(sender, e)
		
	end

	def Label1Click(sender, e)
		
	end

	def Label2Click(sender, e)
		
	end
	

	def Label3Click(sender, e)
		
	end

	def Label4Click(sender, e)
		
	end
end
import pexpect
import sys, os
import time
import subprocess


class SmartHomeUtility(object):
    def __init__(self, dut_dsn):
        self.child = None

        self.dut_dsn = dut_dsn
        print('DUT DSN: {0}'.format(self.dut_dsn))

        # self.bulb_bd_addr_list = bulb_bd_addr_list
        # print 'Bulb BD address list: {0}'.format(self.bulb_bd_addr_list)

        self.bulb_index_list = list()

        self.bulb_dict = dict()

        self.cmd_lanuch = 'smarthome_utility_puffin'
        self.cmd_start_discovery = '1'
        self.cmd_get_discovered_devices = '2'
        self.cmd_quit = '0'
        self.cmd_back = '-1'
        self.cmd_list = '-2'
        self.cmd_bulk_commands = '-3'
        self.power = "1"
        self.unpair_index = '-6'

        self.bulb_index = None
        self.mock_index = None
        self.turn_on_index = '3'
        self.turn_off_index = '4'

        self.adb_shell()
        self.shu_launch()
        self.shu_get_discovered_devices()
        self.bulk_control()
        self.bulk_control_power_list()

    def take_a_break(self, sleep_in_sec=3, post_fix=''):

        print('Sleep for {0} sec(s) {1}'.format(sleep_in_sec, post_fix))
        time.sleep(sleep_in_sec)

    def adb_shell(self):

        child = pexpect.spawn('adb -s {0} shell'.format(self.dut_dsn), encoding='utf-8')
        child.logfile_send = sys.stdout
        index = child.expect(["#", pexpect.TIMEOUT])
        if index == 0:
            print('Enter adb shell successfully for DUT {0}'.format(self.dut_dsn))
            self.child = child
            time.sleep(2)
            return True
        else:
            raise Exception('Fail to open adb shell for DUT {0}'.format(self.dut_dsn))

    def shu_launch(self):

        self.child.sendline(self.cmd_lanuch)
        index = self.child.expect(["0 - quit", pexpect.TIMEOUT])
        if index == 0:
            print('Launch SmartHomeUtility successfully')
            time.sleep(2)
            return True
        else:
            raise Exception('Fail to lanuch SmartHomeUtility')

    def shu_get_discovered_devices(self):

        self.child.sendline(self.cmd_get_discovered_devices)
        index = self.child.expect(["0 - quit", pexpect.TIMEOUT])
        if index == 0:
            print('Launch get_discovered_devices successfully')
            time.sleep(2)
            return True
        else:
            raise Exception('Fail to lanuch get_discovered_devices')

    def display_list(self):

        self.child.sendline(self.cmd_list)
        index = self.child.expect(["0 - quit", pexpect.TIMEOUT])
        if index == 0:
            print('Display SHU list successfully')
            return True
        else:
            raise Exception('Fail to display SHU list')

    def bulk_control(self):

        self.child.sendline(self.cmd_bulk_commands)
        index = self.child.expect(["0 - quit", pexpect.TIMEOUT])
        if index == 0:
            print('Display bulk command list successfully')
            return True
        else:
            raise Exception('Fail to display bulk command list')

    def bulk_control_power_list(self):

        self.child.sendline(self.power)
        index = self.child.expect(["0 - quit", pexpect.TIMEOUT])
        if index == 0:
            print('Display bulk command list successfully')
            return True
        else:
            raise Exception('Fail to display bulk command list')

    def bulk_control_power(self, toggle='on'):

        if toggle == 'on':
            power_toggle = "1"
        elif toggle == "off":
            power_toggle = "2"
        self.child.sendline(power_toggle)
        index = self.child.expect(["0 - quit", pexpect.TIMEOUT])
        if index == 0:
            print('Display power{} successfully'.format("on"))
            return True
        else:
            raise Exception('Fail to display bulk command list')

    # def back(self, menu_str='get_discovered_devices', log_str='previous SHU list'):
    # 	self.child.sendline(self.cmd_back)
    # 	index = self.child.expect([menu_str, pexpect.TIMEOUT])
    # 	if index == 0:
    # 		print('Back to {0} successfully'.format(log_str))
    # 		return True
    # 	else:
    # 		raise Exception('Error back to {0}'.format(log_str))

    def quit_utl(self):

        self.child.sendline(self.cmd_quit)
        index = self.child.expect(["#", pexpect.TIMEOUT])
        if index == 0:
            print('Exit SHU successfully')
            time.sleep(3)
            return True
        else:
            raise Exception('Fail to exit SHU')


# def start_discovery(self):
# 	print 'SHU starting discovery...'
# 	self.child.sendline(self.cmd_start_discovery)
# 	self.take_a_break(60, post_fix='after sending discovery cmd')
# 	index = self.child.expect(["Starting Discovery at", pexpect.TIMEOUT])
# 	if index == 0:
# 		print 'Send start discovery cmd successfully'
# 		self.unpair_mock_device()
# 		self.get_bulb_index()
# 		# self.shu_get_turn_on_index()
# 		# self.shu_get_turn_off_index()
# 		return True
# 	else:
# 		raise Exception('Fail to send start discovery cmd')
#
# def get_mock_device_index(self):
# 	print 'Getting Mock device index...'
# 	self.child.sendline(self.cmd_get_discovered_devices)
# 	index = self.child.expect(['MockPairableDevice', pexpect.TIMEOUT])
# 	if index == 0:
# 		print 'Enter discovered devices menu and found Mock device successfully'
# 		time.sleep(2)
# 		if self.child.before[-4].isdigit():
# 			self.mock_index = self.child.before[-4]
# 			print 'mock_index: {0}'.format(self.mock_index)
# 			if self.back(menu_str='start_discovery', log_str='main menu'):
# 				return True
# 		else:
# 			raise Exception('Error Mock device index found is not integer')
# 	else:
# 		print 'Fail to enter discovered devices or find Mock device menu'

# def unpair_mock_device(self):
# 	if self.get_mock_device_index():
# 		if self.unpair(mock=True):
# 			print 'Unpair Mock device successfully'
# 			return True
# 		else:
# 			raise Exception('Fail to unpair Mock device')
#
# 	else:
# 		raise Exception('Fail to get mock device index')
#
# 	return False

# def get_bulb_index(self):
# 	print 'Getting paired bulb index...'
# 	if not self.bulb_bd_addr_list:
# 		raise Exception('Bulb BD addr list is empty')
# 	else:
# 		for i_addr in self.bulb_bd_addr_list:
# 			self.child.sendline(self.cmd_get_discovered_devices)
# 			index = self.child.expect([i_addr, pexpect.TIMEOUT])
# 			if index == 0:
# 				print 'Enter discovered devices menu successfully'
# 				time.sleep(2)
# 				if self.child.before[-4].isdigit():
# 					self.bulb_index_list.append(self.child.before[-4])
# 					print '{0} bulb_index: {1}'.format(i_addr, self.child.before[-4])
# 					if self.back(menu_str='start_discovery', log_str='main menu'):
# 						pass
# 					else:
# 						raise Exception('Fail to back to main menu')
# 				else:
# 					raise Exception('Error bulb index found is not integer')
# 			else:
# 				raise Exception('Fail to enter discovered devices menu')
#
# 		if len(self.bulb_index_list) == len(self.bulb_bd_addr_list):
# 			print 'Got all paired bulb index'
# 			self.bulb_dict = dict(zip(self.bulb_bd_addr_list, self.bulb_index_list))
# 			print self.bulb_dict
# 			print 'Empty out self.bulb_index_list'
# 			self.bulb_index_list = list()
# 			return True
# 		else:
# 			raise Exception('bulb_index_list length is not as same as bulb_bd_addr_list')
#
# 	return False
#
# def get_turn_on_index(self):
# 	print('Getting turn on action index')
# 	self.child.sendline(self.bulb_index)
# 	index = self.child.expect(['Alexa.PowerController.TurnOn', pexpect.TIMEOUT])
# 	if index == 0:
# 		print 'Enter bulb {0} menu successfully'.format(self.bulb_index)
# 		time.sleep(1)
# 		self.turn_on_index = self.child.before[-4]
# 		print 'turn_on_index: {0}'.format(self.turn_on_index)
# 		return True
# 	else:
# 		raise Exception('Fail to enter bulb {0} menu menu'.format(self.bulb_index))
#
# 	return False
#
# def get_turn_off_index(self):
# 	print 'Getting turn off action index'
# 	self.child.sendline(self.bulb_index)
# 	index = self.child.expect(['Alexa.PowerController.TurnOff', pexpect.TIMEOUT])
# 	if index == 0:
# 		print 'Enter bulb {0} menu successfully'.format(self.bulb_index)
# 		time.sleep(1)
# 		self.turn_off_index = self.child.before[-4]
# 		print 'turn_off_index: {0}'.format(self.turn_off_index)
# 		return True
# 	else:
# 		raise Exception('Fail to enter bulb {0} menu menu'.format(self.bulb_index))
#
# 	return False
#
# def turn_on(self, bulb_bd_addr_list=None, vui=True):
# 	if vui:
# 		subprocess.call('alexa turn on home', shell=True)
# 		self.take_a_break(15, post_fix='after sending turn on cmd')
# 	else:
# 		if bulb_bd_addr_list is None:
# 			bulb_bd_addr_list = self.bulb_bd_addr_list
#
# 		for i_addr in bulb_bd_addr_list:
# 			print 'Turning on {0}'.format(i_addr)
# 			self.child.sendline(self.cmd_get_discovered_devices)
# 			index = self.child.expect([i_addr, pexpect.TIMEOUT])
# 			if index == 0:
# 				print 'Enter paired device list menu, and found {0}'.format(i_addr)
# 				self.child.sendline(self.bulb_dict[i_addr])
# 				index = self.child.expect(['FactoryReset', pexpect.TIMEOUT])
# 				if index == 0:
# 					print 'Entered {0} control menu'.format(i_addr)
# 					self.child.sendline(self.turn_on_index)
# 					index = self.child.expect(["FactoryReset", pexpect.TIMEOUT])
# 					if index == 0:
# 						print 'Send turn on cmd successfully'
# 						self.take_a_break(10, post_fix='after sending turn on cmd')
# 						if self.back(menu_str='bulk_commands', log_str='paired device menu'):
# 							if self.back(menu_str='start_discovery', log_str='main menu'):
# 								pass
# 							else:
# 								raise Exception('Fail to back to main menu')
# 						else:
# 							raise Exception('Fail to back to paired device menu')
# 					else:
# 						raise Exception('Fail to send turn on cmd')
# 				else:
# 					raise Exception('Fail to enter {0} control menu'.format(i_addr))
# 			else:
# 				raise Exception('Fail to enter device list menu or find {0}'.format(i_addr))
#
# 		return True
#
# def turn_off(self, bulb_bd_addr_list=None, vui=True):
# 	if vui:
# 		subprocess.call('alexa turn off home', shell=True)
# 		self.take_a_break(15, post_fix='after sending turn off cmd')
# 	else:
# 		if bulb_bd_addr_list is None:
# 			bulb_bd_addr_list = self.bulb_bd_addr_list
#
# 		for i_addr in bulb_bd_addr_list:
# 			print 'Turning off {0}'.format(i_addr)
# 			self.child.sendline(self.cmd_get_discovered_devices)
# 			index = self.child.expect([i_addr, pexpect.TIMEOUT])
# 			if index == 0:
# 				print 'Enter paired device list menu, and found {0}'.format(i_addr)
# 				self.child.sendline(self.bulb_dict[i_addr])
# 				index = self.child.expect(['FactoryReset', pexpect.TIMEOUT])
# 				if index == 0:
# 					print 'Entered {0} control menu'.format(i_addr)
# 					self.child.sendline(self.turn_off_index)
# 					index = self.child.expect(["FactoryReset", pexpect.TIMEOUT])
# 					if index == 0:
# 						print 'Send turn off cmd successfully'
# 						self.take_a_break(10, post_fix='after sending turn off cmd')
# 						if self.back(menu_str='bulk_commands', log_str='paired device menu'):
# 							if self.back(menu_str='start_discovery', log_str='main menu'):
# 								pass
# 							else:
# 								raise Exception('Fail to back to main menu')
# 						else:
# 							raise Exception('Fail to back to paired device menu')
# 					else:
# 						raise Exception('Fail to send turn off cmd')
# 				else:
# 					raise Exception('Fail to enter {0} control menu'.format(i_addr))
# 			else:
# 				raise Exception('Fail to enter device list menu or find {0}'.format(i_addr))
#
# 		return True
#
# def unpair(self, bulb_bd_addr_list=None, mock=False):
# 	if mock:
# 		print 'Unpairing Mock device...'
# 		self.child.sendline(self.cmd_get_discovered_devices)
# 		index = self.child.expect(['MockPairableDevice', pexpect.TIMEOUT])
# 		if index == 0:
# 			print 'Enter paired device list menu, and found Mock device'
# 			time.sleep(2)
# 			self.child.sendline(self.mock_index)
# 			index = self.child.expect(['unPair', pexpect.TIMEOUT])
# 			if index == 0:
# 				print 'Entered Mock device control menu'
# 				self.child.sendline(self.unpair_index)
# 				index = self.child.expect(["unPair", pexpect.TIMEOUT])
# 				if index == 0:
# 					print 'Send unpair cmd successfully'
# 					self.take_a_break(3, post_fix='after sending unpair cmd')
# 					if self.back(menu_str='bulk_commands', log_str='paired device menu'):
# 						if self.back(menu_str='start_discovery', log_str='main menu'):
# 							pass
# 						else:
# 							raise Exception('Fail to back to main menu')
# 					else:
# 						raise Exception('Fail to back to paired device menu')
# 				else:
# 					raise Exception('Fail to send unpair cmd')
# 			else:
# 				raise Exception('Fail to enter Mock device control menu')
# 		else:
# 			raise Exception('Fail to enter device list menu or find Mock device')
#
# 		return True
#
# 	else:
# 		if bulb_bd_addr_list is None:
# 			bulb_bd_addr_list = self.bulb_bd_addr_list
#
# 		for i_addr in bulb_bd_addr_list:
# 			print 'Unpairing {0}'.format(i_addr)
# 			self.child.sendline(self.cmd_get_discovered_devices)
# 			index = self.child.expect([i_addr, pexpect.TIMEOUT])
# 			# print self.child.before
# 			# print self.child.after
# 			if index == 0:
# 				print 'Enter paired device list menu, and found {0}'.format(i_addr)
# 				if self.child.before[-4].isdigit():
# 					self.child.sendline(self.child.before[-4])
# 					index = self.child.expect(['FactoryReset', pexpect.TIMEOUT])
# 					if index == 0:
# 						print 'Entered {0} control menu'.format(i_addr)
# 						self.child.sendline(self.unpair_index)
# 						index = self.child.expect(["FactoryReset", pexpect.TIMEOUT])
# 						if index == 0:
# 							print 'Send unpair cmd successfully'
# 							self.take_a_break(3, post_fix='after sending unpair cmd')
# 							if self.back(menu_str='bulk_commands', log_str='paired device menu'):
# 								if self.back(menu_str='start_discovery', log_str='main menu'):
# 									pass
# 								else:
# 									raise Exception('Fail to back to main menu')
# 							else:
# 								raise Exception('Fail to back to paired device menu')
# 						else:
# 							raise Exception('Fail to send unpair cmd')
# 					else:
# 						raise Exception('Fail to enter {0} control menu'.format(i_addr))
# 				else:
# 					raise Exception('Error bulb index found is not integer')
# 			else:
# 				raise Exception('Fail to enter device list menu or find {0}'.format(i_addr))
#
# 		return True


shu = SmartHomeUtility(dut_dsn='G8M11M09018201QU')

for i in range(10):
    print('######## Iteration {0} ########'.format(i + 1))
    shu.bulk_control_power(toggle='on')
    shu.take_a_break(7, "Sleep between each toggle iterations")
    shu.bulk_control_power(toggle='off')
    shu.take_a_break(7, "Sleep between each toggle iterations")

shu.quit_utl()

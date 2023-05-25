from web3 import Web3
import requests
import cfscrape
import json
import time
from dotenv import load_dotenv
load_dotenv()
import os


api_url ='api.bscscan.com'
YOUR_API_KEY = "YGU4ZK9PXZUU786QB5WECN5WKINDNMW8DV"

Main_Address = os.getenv("Main_Address")
Main_Key = os.getenv("Main_Key")

Busd_Contract_Address = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
Busd_Contract_Abi = json.loads(
  '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
)

Sale_GA_Contract_Address = '0x6077f85D7699CB763056BDe7bbf7507e9509d034'
Sale_FCFS_Contract_Address = '0x4914d8c52b3130E128A2DAA489e6d5a79dcF6200'
Sale_FCFS_2_Contract_Address = '0x3023D93C1B6fe70f24d1F22dEf28CBD054ff05C1'
Sale_Contract_Address= '0x63c7008B063B9aE48482E93ACAD8AfF0dcBbd460'
Sale_Contract_Abi = json.loads('[{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getUserInfo","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getAllocation","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"toggleWhitelist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"whitelist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"whitelistMultiple","outputs":[],"stateMutability":"nonpayable","type":"function"}]')


bsc_url = "https://bsc-dataseed1.binance.org"
polygon_url = 'https://rpc.ankr.com/polygon'
web3 = Web3(Web3.HTTPProvider(polygon_url))  # 建立连接


# bnb_balance = web3j.fromWei(int(bnb_balance), "ether")

def gettime():
  return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def getBusdBalance(_address):
  contract_address = Web3.toChecksumAddress(Busd_Contract_Address)
  main_add = Web3.toChecksumAddress(_address)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)

  res = contract.functions.balanceOf(main_add).call()
  balance = res / 10 ** 6
  print("Busd余额为："+str(balance))
  return  balance
#获取分配的额度
def getAllocation(_address):
  contract_address = Web3.toChecksumAddress(Sale_Contract_Address)
  main_add = Web3.toChecksumAddress(_address)
  contract = web3.eth.contract(address=contract_address, abi=Sale_Contract_Abi)
  res = contract.functions.getAllocation(main_add).call()
  allocation = res / 10 ** 18
  print("分配的额度为："+str(allocation))
  return  allocation

def transferBusd(_mainAddress,_mainKey,_num):
  contract_address = Web3.toChecksumAddress(Busd_Contract_Address)
  main_add = Web3.toChecksumAddress(_mainAddress)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice


  txn = contract.functions.transfer('0xF703A4ADeD9797587e795eE12862dc3Bab7F8146',web3.toWei(_num, 'ether')).buildTransaction({
      'nonce': nonce,
      'value': web3.toWei(0, 'ether'),
      'gas': 210000,
      'gasPrice': gas_price,
  })

  signed_tx = web3.eth.account.signTransaction(txn, _mainKey)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def transferHalo(_mainAddress,_mainKey,_num):
  contract_address = Web3.toChecksumAddress(Halo_Contract_Address)
  main_add = Web3.toChecksumAddress(_mainAddress)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice


  txn = contract.functions.transfer('0xF703A4ADeD9797587e795eE12862dc3Bab7F8146',web3.toWei(_num, 'ether')).buildTransaction({
      'nonce': nonce,
      'value': web3.toWei(0, 'ether'),
      'gas': 210000,
      'gasPrice': gas_price,
  })

  signed_tx = web3.eth.account.signTransaction(txn, _mainKey)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def batchBusd(_mainAddress,_num):
  contract_address = Web3.toChecksumAddress(Busd_Contract_Address)
  main_add = Web3.toChecksumAddress(Main_Address)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)
  to_address = Web3.toChecksumAddress(_mainAddress)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice


  txn = contract.functions.transfer(to_address,web3.toWei(_num, 'ether')).buildTransaction({
      'nonce': nonce,
      'value': web3.toWei(0, 'ether'),
      'gas': 210000,
      'gasPrice': gas_price,
  })

  signed_tx = web3.eth.account.signTransaction(txn, Main_Key)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def batchBusdForPolygon(_mainAddress,_num):
  contract_address = Web3.toChecksumAddress(Busd_Contract_Address)
  main_add = Web3.toChecksumAddress(Main_Address)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)
  to_address = Web3.toChecksumAddress(_mainAddress)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice


  txn = contract.functions.transfer(to_address,int(_num)*1000000).buildTransaction({
      'nonce': nonce,
      'value': web3.toWei(0, 'ether'),
      'gas': 210000,
      'gasPrice': gas_price,
  })

  signed_tx = web3.eth.account.signTransaction(txn, Main_Key)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def pad_purchase_amount(amount_hex: str) -> str:
    padding_length = 64 - len(amount_hex)
    return '0' * padding_length + amount_hex


def approveBusdToSale(_mainAddress,_mainKey,purchase_amount):
  contract_address = Web3.toChecksumAddress(Busd_Contract_Address)
  main_add = Web3.toChecksumAddress(_mainAddress)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)
  sale_address = Web3.toChecksumAddress(Sale_Contract_Address)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice

  txn = contract.functions.approve(sale_address,web3.toWei(purchase_amount, 'ether')).buildTransaction({
      'nonce': nonce,
      'value': web3.toWei(0, 'ether'),
      'gas': 210000,
      'gasPrice': gas_price,
  })

  signed_tx = web3.eth.account.signTransaction(txn, _mainKey)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def approveBusdToSaleForPolygon(_mainAddress,_mainKey,purchase_amount):
  contract_address = Web3.toChecksumAddress(Busd_Contract_Address)
  main_add = Web3.toChecksumAddress(_mainAddress)
  contract = web3.eth.contract(address=contract_address, abi=Busd_Contract_Abi)
  sale_address = Web3.toChecksumAddress(Sale_Contract_Address)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice

  txn = contract.functions.approve(sale_address,purchase_amount * 1000000).buildTransaction({
      'nonce': nonce,
      'value': web3.toWei(0, 'ether'),
      'gas': 210000,
      'gasPrice': gas_price,
  })

  signed_tx = web3.eth.account.signTransaction(txn, _mainKey)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def buy(_mainAddress,_mainKey,purchase_amount):
  contract_address = Web3.toChecksumAddress(Sale_Contract_Address)
  main_add = Web3.toChecksumAddress(_mainAddress)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice

  purchase_amount = Web3.toWei(purchase_amount, "ether")
  purchase_amount_hex = web3.toHex(purchase_amount)[2:]
  print(purchase_amount_hex)
  padded_purchase_amount = pad_purchase_amount(purchase_amount_hex)
  print(padded_purchase_amount)

  txn = {
    'chainId': 137,
    'from': main_add,
    'to': contract_address,
    'value': web3.toWei(0, 'ether'),
    'gas': 2000000,
    'gasPrice': gas_price,
    'nonce': nonce,
    'data': '0x447f7fdb' + padded_purchase_amount
  }

  gas = web3.eth.estimateGas(txn)
  print("gas:"+str(gas))

  txn = {
    'chainId': 137,
    'from': main_add,
    'to': contract_address,
    'value': web3.toWei(0, 'ether'),
    'gas': gas,
    'gasPrice': gas_price,
    'nonce': nonce,
    'data': '0x447f7fdb' + padded_purchase_amount
  }

  signed_tx = web3.eth.account.signTransaction(txn, _mainKey)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash

def claim(_mainAddress,_mainKey,claim_contract_address):
  contract_address = Web3.toChecksumAddress(claim_contract_address)
  main_add = Web3.toChecksumAddress(_mainAddress)

  nonce = web3.eth.getTransactionCount(main_add)
  print("nonce:"+str(nonce))
  gas_price = web3.eth.gasPrice

  txn = {
    'from': main_add,
    'to': contract_address,
    'value': web3.toWei(0, 'ether'),
    'gas': 200000,
    'gasPrice': gas_price,
    'nonce': nonce,
    'data': '0x86d1a69f'
  }

  gas = web3.eth.estimateGas(txn)
  print("gas:"+str(gas))

  txn = {
    'from': main_add,
    'to': contract_address,
    'value': web3.toWei(0, 'ether'),
    'gas': gas,
    'gasPrice': gas_price,
    'nonce': nonce,
    'data': '0x86d1a69f'
  }

  signed_tx = web3.eth.account.signTransaction(txn, _mainKey)
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
  hash = web3.toHex(tx_hash)
  print(hash)
  return  hash
# .env文件配置主账号和私钥

def go():
  fo = open("/Users/lu/vscodeWorkSpace/撸毛脚本/evmTools/wepad-chao.txt","r")
  lines = [l.replace('\n','').split('----') for l in fo if l.strip()]
  print(lines)
  print(len(lines))
  a=[]
  num = 0
  for i in range(len(lines)):
    if(i>=0):
      print(lines[i][1])
      # 获取分配的额度
      allocation = getAllocation(lines[i][1])
      num = num + int(allocation)
      # 批量转账busd
      # hash = batchBusd(lines[i][1],int(allocation))
      # hash = batchBusdForPolygon(lines[i][1],int(allocation))
      # time.sleep(30)
      # 获取busd余额
      # balance = getBusdBalance(lines[i][1])
      # 授权busd给sale合约
      # hash = approveBusdToSale(lines[i][1],lines[i][2],25)
      # hash = approveBusdToSaleForPolygon(lines[i][1],lines[i][2],int(allocation))
      # 购买
      hash = buy(lines[i][1],lines[i][2],int(allocation))
      # 领取
      # hash = claim(lines[i][1],lines[i][2],Sale_GA_Contract_Address)
  print("总额度："+str(num))
  
go()
# /usr/local/bin/python3 /Users/lu/vscodeWorkSpace/撸毛脚本/evmTools/wepad.py
      
# while(True):
#   time.sleep(1)
#   print("当前时间："+gettime())
#   try:
#     go()
#   except Exception as e:
#     print(e)


  



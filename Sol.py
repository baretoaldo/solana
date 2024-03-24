# Program untuk otomatis mengirim semua SOL dari private key di jaringan Solana ke alamat Anda
# Hanya untuk keperluan hiburan, jangan digunakan untuk tindakan ilegal atau merugikan

# Import library yang diperlukan
from solana.account import Account
from solana.rpc.api import Client
from solana.transaction import Transaction

# Inisialisasi koneksi ke jaringan Solana
rpc_url = 'https://api.mainnet-beta.solana.com'  # Atau gunakan RPC URL yang sesuai
client = Client(rpc_url)

# Definisikan private key Anda
private_key = '3nD4t2hSEwrSAiTy91TTgJ3CyMWSQLTjA5EcyBMWrGShta9RgcbSGEkY6PCAEeZDeKksjkXvGKqdvru9gqoeZLPV'

# Definisikan alamat tujuan
tujuan = '7XpGaFbPcb6Nz73KPVzzun72RJGN475dUMQH8nCVwkqf'

# Buat objek akun dari private key
akun = Account(private_key)

# Dapatkan saldo Solana dari alamat
saldo_solana = client.get_balance(akun.public_key())

# Tampilkan saldo Solana
print('Saldo Solana dari alamat Anda:', saldo_solana)

# Kirim semua SOL ke alamat tujuan
transaksi = Transaction().add(
    spl_token.transfer(
        akun.public_key(),
        akun.public_key(),
        tujuan,
        saldo_solana
    )
)

# Tandatangani transaksi
transaksi.sign(akun)

# Kirim transaksi ke jaringan Solana
txid = client.send_transaction(transaksi, akun)
print('Transaksi berhasil! TXID:', txid)
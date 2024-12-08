import paramiko

# Membuat objek SSHClient
ssh_client = paramiko.SSHClient()

# Menambahkan server ke daftar known hosts secara otomatis
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Menghubungkan ke server SSH
try:
    # Masukkan informasi server
    ssh_client.connect(
        hostname="192.168.1.2",  # Ganti dengan alamat IP server Anda
        port=22,                   # Port SSH standar
        username="gilangrp",           # Ganti dengan username Anda
        password="@Gilang123"          # Ganti dengan password Anda
    )
    print("Koneksi berhasil!")

    # Menjalankan perintah di server
    stdin, stdout, stderr = ssh_client.exec_command('ls -l')

    # Membaca dan menampilkan hasil output
    output = stdout.read().decode()
    error = stderr.read().decode()

    if output:
        print("Output:")
        print(output)
    if error:
        print("Error:")
        print(error)

except paramiko.AuthenticationException:
    print("Autentikasi gagal, periksa username atau password.")
except paramiko.SSHException as sshException:
    print(f"SSH error terjadi: {sshException}")
except Exception as e:
    print(f"Error lain terjadi: {e}")
finally:
    # Menutup koneksi SSH
    ssh_client.close()
    print("Koneksi SSH ditutup.")

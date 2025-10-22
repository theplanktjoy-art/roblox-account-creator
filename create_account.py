import requests
import random
import string
from datetime import datetime
import json

def generate_random_username():
    """Generate username acak yang menarik"""
    prefixes = ['Super', 'Pro', 'Epic', 'Cool', 'Mega', 'Ultra', 'Cyber', 'Dark', 'Fire', 'Ice']
    suffixes = ['Gamer', 'Player', 'Master', 'King', 'Ninja', 'Hero', 'Legend', 'Warrior', 'Dragon']
    
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    number = ''.join(random.choices(string.digits, k=4))
    
    return f"{prefix}{suffix}{number}"

def generate_random_password():
    """Generate password yang kuat dan aman"""
    # Password harus minimal 8 karakter, mengandung huruf besar, kecil, dan angka
    uppercase = ''.join(random.choices(string.ascii_uppercase, k=3))
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=3))
    digits = ''.join(random.choices(string.digits, k=4))
    special = random.choice('!@#$%')
    
    # Gabungkan dan acak
    password_list = list(uppercase + lowercase + digits + special)
    random.shuffle(password_list)
    
    return ''.join(password_list)

def generate_random_birthday():
    """Generate tanggal lahir acak (usia 13-25 tahun)"""
    year = random.randint(1998, 2011)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}T00:00:00.000Z"

def create_roblox_account():
    """Membuat akun Roblox baru secara otomatis"""
    
    print("=" * 60)
    print("🎮 ROBLOX AUTOMATIC ACCOUNT CREATOR")
    print("=" * 60)
    print()
    
    # Generate data akun secara otomatis
    username = generate_random_username()
    password = generate_random_password()
    birthday = generate_random_birthday()
    gender = random.choice([2, 3])  # 2 = male, 3 = female
    
    print("📝 Generating account credentials...")
    print(f"   ├─ Username: {username}")
    print(f"   ├─ Password: {password}")
    print(f"   └─ Birthday: {birthday.split('T')[0]}")
    print()
    
    # URL endpoint Roblox untuk signup
    signup_url = "https://auth.roblox.com/v2/signup"
    
    # Data yang diperlukan untuk membuat akun
    payload = {
        "username": username,
        "password": password,
        "birthday": birthday,
        "gender": gender,
        "isTosAgreementBoxChecked": True,
        "context": "MultiverseSignupForm"
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Origin": "https://www.roblox.com",
        "Referer": "https://www.roblox.com/"
    }
    
    try:
        print("🔄 Creating Roblox account...")
        print()
        
        # Kirim request untuk membuat akun
        response = requests.post(signup_url, json=payload, headers=headers, timeout=30)
        
        print("📡 Server Response:")
        print(f"   Status Code: {response.status_code}")
        print()
        
        if response.status_code == 200:
            response_data = response.json()
            
            print("✅ SUCCESS! Account created successfully!")
            print()
            print("=" * 60)
            print("🎉 YOUR NEW ROBLOX ACCOUNT")
            print("=" * 60)
            print(f"Username      : {username}")
            print(f"Password      : {password}")
            print(f"Birthday      : {birthday.split('T')[0]}")
            print(f"Created At    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("=" * 60)
            print()
            
            # Simpan ke file dengan format yang lebih rapi
            with open("account_info.txt", "w", encoding="utf-8") as f:
                f.write("=" * 60 + "\n")
                f.write("🎮 ROBLOX ACCOUNT INFORMATION\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Username      : {username}\n")
                f.write(f"Password      : {password}\n")
                f.write(f"Birthday      : {birthday.split('T')[0]}\n")
                f.write(f"Created At    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("=" * 60 + "\n")
                f.write("⚠️  IMPORTANT: Keep this information safe!\n")
                f.write("🔗 Login at: https://www.roblox.com/login\n")
                f.write("=" * 60 + "\n")
            
            # Simpan juga dalam format JSON
            account_data = {
                "username": username,
                "password": password,
                "birthday": birthday.split('T')[0],
                "created_at": datetime.now().isoformat(),
                "success": True
            }
            
            with open("account_info.json", "w", encoding="utf-8") as f:
                json.dump(account_data, f, indent=2)
            
            print("💾 Account information saved to:")
            print("   ├─ account_info.txt")
            print("   └─ account_info.json")
            print()
            print("🔗 Login URL: https://www.roblox.com/login")
            print()
            
            return True
            
        else:
            print("❌ FAILED! Could not create account")
            print()
            print("Error Details:")
            try:
                error_data = response.json()
                print(json.dumps(error_data, indent=2))
            except:
                print(response.text)
            print()
            print("⚠️  Possible reasons:")
            print("   • Roblox requires CAPTCHA verification")
            print("   • Username already taken")
            print("   • IP address rate limited")
            print("   • Additional verification required")
            print()
            
            # Tetap simpan informasi untuk referensi
            with open("failed_attempt.txt", "w", encoding="utf-8") as f:
                f.write(f"Failed attempt\n")
                f.write(f"Username: {username}\n")
                f.write(f"Password: {password}\n")
                f.write(f"Status Code: {response.status_code}\n")
                f.write(f"Response: {response.text}\n")
            
            return False
            
    except requests.exceptions.Timeout:
        print("❌ ERROR: Request timeout")
        print("   The server took too long to respond")
        return False
        
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Connection failed")
        print("   Could not connect to Roblox servers")
        return False
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        print(f"   Type: {type(e).__name__}")
        return False

if __name__ == "__main__":
    success = create_roblox_account()
    
    print()
    if success:
        print("✨ Process completed successfully!")
    else:
        print("⚠️  Process completed with errors")
        print("💡 Try running the script again or create account manually")
    
    print("=" * 60)

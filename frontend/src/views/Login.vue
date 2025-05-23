<script setup>
import { login } from '@/assets/scripts/django_api_calls';
import { userState } from '@/assets/scripts/userState';
import router from '@/router';
import { ref } from 'vue';
const username = ref('');
const password = ref('');
</script>

<template>
    <div class="login-container">
        <h1>Login</h1>
        <form @submit.prevent="handleLogin">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" placeholder="Enter your username" required />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" placeholder="Enter your password" required />
            
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
async function handleLogin() {
    if (username.value && password.value) {
        try {
            const data = await login(username.value, password.value);
            console.log('Login succesful:', data)
            // Update the shared user state
            userState.userName = data.user.username;
            userState.userEmail = data.user.email;
            userState.firstName = data.user.first_name;
            userState.lastName = data.user.last_name;
            console.log(userState)
            //Redirect to profile page
            router.push('/profile')
        } catch (error) {
            alert("Login failed: ", error);
        }
    } else {
        alert('Please fill in all fields');
    }

}
</script>

<style scoped>
.login-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
}

h1 {
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
    text-align: left;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>

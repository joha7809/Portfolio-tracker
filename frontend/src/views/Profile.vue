<!-- Vue page for viewing Profile Page  ---> 
<script setup>
const userName = "Testing"
const userEmail = "test@email.com"
var userBio = "This is a test bio"
</script>

<template>
  <div class="profile">
    <h1>Profile</h1>
    <div class="profile-info">
      <h2>{{ userName }}</h2>
      <p>Email: {{ userEmail }}</p>
      <p>Bio: {{ userBio }}</p>
    </div>
    <div class="profile-actions">
      <button @click=logout>Logout</button>
      <button @click=editProfile>Edit Profile</button>
    </div>
  </div>
</template>

<!--edit profile button -->
<script edit_profile>
  // When logout pressed, post request to /api/logout for ending session
  // csrf token should be passed
  async function logout() {
    try {
      const response = await fetch('/api/logout/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken(), // Ensure you have a function to retrieve the CSRF token
        },
      });

      if (response.ok) {
        alert('Logged out successfully');
        // Redirect to login page or perform other actions
        window.location.href = '/login';
      } else {
        const errorData = await response.json();
        console.error('Logout failed:', errorData);
        alert('Failed to log out. Please try again.');
      }
    } catch (error) {
      console.error('Error during logout:', error);
      alert('An error occurred. Please try again.');
    }
  }

  function getCsrfToken() {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];
    return cookieValue || '';
  }
</script>


<style scoped>
.profile {
  padding: 20px;
  /* background-color: #70aafb; */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.profile h1 {
  font-size: 24px;
  margin-bottom: 20px;
}
.profile-info {
  margin-bottom: 20px;
}
.profile-info h2 {
  font-size: 20px;
  margin-bottom: 10px;
}
.profile-info p {
  font-size: 16px;
  margin: 5px 0;
}
.profile-actions {
  display: flex;
  gap: 10px;
}
.profile-actions button {
  padding: 10px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.profile-actions button:hover {
  background-color: #007bff;
  color: white;
}
.profile-actions button:active {
  background-color: #0056b3;
}
.profile-actions button:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.5);
}
</style>


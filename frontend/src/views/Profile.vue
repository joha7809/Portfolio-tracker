<!-- Vue page for viewing Profile Page  --->
<script setup>
import { logout } from "@/assets/scripts/django_api_calls";
import { userState } from "@/assets/scripts/userState";
var userBio = "This is a test bio";
</script>

<template>
  <div class="profile">
    <h1>Profile</h1>
    <div class="profile-info">
      <h2>{{ userState.userName }}</h2>
      <p>Email: {{ userState.userEmail }}</p>
      <p>Username: {{ userState.userName }}</p>
      <p>first name: {{ userState.firstName }}</p>
      <p>last name: {{ userState.lastName }}</p>
      <p>Bio: {{ userBio }}</p>
    </div>
    <div class="profile-actions">
      <button @click="logout">Logout</button>
      <button @click="editProfile">Edit Profile</button>
    </div>
  </div>
</template>

<!--edit profile button -->
<script edit_profile></script>

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

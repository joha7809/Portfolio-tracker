function getCsrfToken() {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];
    return cookieValue || '';
}

// Function to log out the user
export async function logout() {
    try {
        const response = await fetch('/api/logout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
        });

        if (response.ok) {
            alert('Logged out successfully');
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

// Function to log in the user
export async function login(username, password) {
    try {
        const response = await fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Login successful:', data);
            return data;
        } else {
            const errorData = await response.json();
            console.error('Login failed:', errorData);
            throw new Error('Login failed');
        }
    } catch (error) {
        console.error('Error during login:', error);
        throw error;
    }
}





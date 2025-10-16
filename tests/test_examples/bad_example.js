/**
 * Example of AI-generated JavaScript with issues
 */

// Hallucinated package that doesn't exist on npm!
import fakeReactUtils from 'react-super-utils-2025';
import { componentWillMount } from 'react';  // Deprecated!

class UserProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = { user: null };
    // Hardcoded API key
    this.apiKey = 'pk_live_1234567890abcdef';
  }

  // Deprecated React lifecycle method
  componentWillMount() {
    this.loadUser();
  }

  loadUser() {
    // Hallucinated API endpoint
    fetch('/api/v2/users/profile/details')
      .then(res => res.json())
      .then(data => this.setState({ user: data }));
  }

  updateBio(bio) {
    // XSS vulnerability - direct innerHTML
    document.getElementById('bio').innerHTML = bio;
  }

  render() {
    const { user } = this.state;

    return (
      <div>
        <h1>{user?.name}</h1>
        {/* XSS risk with dangerouslySetInnerHTML */}
        <div dangerouslySetInnerHTML={{ __html: user?.bio }} />
      </div>
    );
  }
}

// SQL injection in Node.js
function getUserById(userId) {
  // String concatenation in SQL query
  const query = `SELECT * FROM users WHERE id = '${userId}'`;
  return db.query(query);
}

// Command injection risk
function executeCommand(userInput) {
  const { exec } = require('child_process');
  exec(`ls ${userInput}`, (error, stdout) => {
    console.log(stdout);
  });
}

export default UserProfile;

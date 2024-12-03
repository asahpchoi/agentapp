let generatedRoles = [];
let currentTopic = '';

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("container");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function sendMessage() {
    const message = document.getElementById("message").value;
    const rolesText = generatedRoles.map(role => `${role.title}: ${role.description}`).join("\n\n");
    const fullMessage = `Roles:\n${rolesText}\n\nMessage:\n${message}`;
    fetch(`/chat/${encodeURIComponent(fullMessage)}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("chatResponse").innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            document.getElementById("chatResponse").innerText = "Error: " + error;
        });
}

function generateRoles() {
    const topic = document.getElementById("businessTopic").value;
    const numRoles = document.getElementById("numRoles").value;
    currentTopic = topic;
    const loadingIcon = document.getElementById("loadingIcon");
    if (loadingIcon) {
        loadingIcon.style.display = "block";
    }
    fetch('/generate_roles', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: topic, numRoles: numRoles })
    })
    .then(response => response.json())
    .then(data => {
        if (loadingIcon) {
            loadingIcon.style.display = "none";
        }
        const rolesContainer = document.getElementById("rolesResponse");
        if (rolesContainer) {
            rolesContainer.innerHTML = '';
            if (data.roles) {
                generatedRoles = data.roles;
                data.roles.forEach(role => {
                    const roleCard = document.createElement('div');
                    roleCard.className = 'role-card';
                    roleCard.innerHTML = `
                        <div class="role-title">${role.title}</div>
                        <div class="role-description">${role.description}</div>
                    `;
                    rolesContainer.appendChild(roleCard);
                });
                // Show the chat section and save button after roles are generated
                const chatSection = document.getElementById("chatSection");
                const saveRolesButton = document.getElementById("saveRolesButton");
                const startDiscussionButton = document.getElementById("startDiscussionButton");
                if (chatSection) {
                    chatSection.style.display = "block";
                }
                if (saveRolesButton) {
                    saveRolesButton.style.display = "block";
                }
                if (startDiscussionButton) {
                    startDiscussionButton.style.display = "block";
                }
            } else {
                rolesContainer.innerHTML = `<div class="role-card">Error: ${JSON.stringify(data)}</div>`;
            }
        }
    })
    .catch(error => {
        if (loadingIcon) {
            loadingIcon.style.display = "none";
        }
        const rolesContainer = document.getElementById("rolesResponse");
        if (rolesContainer) {
            rolesContainer.innerHTML = `<div class="role-card">Error: ${error}</div>`;
        }
    });
}

function saveRoles() {
    fetch('/save_roles', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: currentTopic, roles: generatedRoles })
    })
    .then(response => response.json())
    .then(data => {
        alert('Roles saved successfully!');
    })
    .catch(error => {
        alert('Error saving roles: ' + error);
    });
}

function startDiscussion() {
    fetch('/start_talk', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: currentTopic, roles: generatedRoles })
    })
    .then(response => response.json())
    .then(data => {
        alert('Discussion started successfully!');
    })
    .catch(error => {
        alert('Error starting discussion: ' + error);
    });
}

window.onload = function() {
    document.getElementById("defaultOpen").click();
    // Initially hide the chat section, save button, and start discussion button
    const chatSection = document.getElementById("chatSection");
    const saveRolesButton = document.getElementById("saveRolesButton");
    const startDiscussionButton = document.getElementById("startDiscussionButton");
    if (chatSection) {
        chatSection.style.display = "none";
    }
    if (saveRolesButton) {
        saveRolesButton.style.display = "none";
    }
    if (startDiscussionButton) {
        startDiscussionButton.style.display = "none";
    }
}

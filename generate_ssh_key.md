To generate an SSH key on a Raspberry Pi for cloning from a Git repository, follow these steps:

1. **Open a terminal on your Raspberry Pi**.

2. **Generate the SSH key**:
    ```sh
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
    - When prompted to "Enter file in which to save the key", you can press Enter to accept the default file location.
    - You can set a passphrase or leave it empty by pressing Enter.

3. **Add the SSH key to the SSH agent**:
    Start the SSH agent in the background:
    ```sh
    eval "$(ssh-agent -s)"
    ```
    Add your SSH private key to the SSH agent:
    ```sh
    ssh-add ~/.ssh/id_rsa
    ```

4. **Copy the SSH key to your clipboard**:
    ```sh
    cat ~/.ssh/id_rsa.pub
    ```
    - Select and copy the output.

5. **Add the SSH key to your GitHub account**:
    - Go to [GitHub SSH keys settings](https://github.com/settings/keys).
    - Click "New SSH key".
    - Paste the copied key into the "Key" field.
    - Give your key a descriptive title.
    - Click "Add SSH key".

6. **Test the SSH connection**:
    ```sh
    ssh -T git@github.com
    ```
    You should see a message like:
    ```
    Hi username! You've successfully authenticated, but GitHub does not provide shell access.
    ```

7. **Clone the Git repository**:
    ```sh
    git clone git@github.com:username/repository.git
    ```

Replace `username` with your GitHub username and `repository` with the name of your repository.

Github link : niteshkvlk/git_assignment_HeroVired

Q1: CalculatorPlus (Complete Git Workflow)
Step 1: Initialize Repository
git init
git remote add origin https://github.com/YOUR_USERNAME/git_assignment_HeroVired.git
git branch -M main
git push -u origin main
________________________________________
Step 2: Create dev Branch
git checkout -b dev
Add your initial calculator code:
import math 
class Calculator:
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    # Square root function implemented
    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":

    calculator = Calculator()

    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # Testing square root feature
    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

git add .
git commit -m "Initial calculator code added"
git push origin dev
 

________________________________________
Step 3: Merge to Main (Version 1)
git checkout main
git merge dev
git push origin main
 
 
________________________________________
Step 4: Create Feature Branch (Square Root)
git checkout dev
git checkout -b feature/sqrt
Add square root code, then:
git add .
git commit -m "Added square root feature"
git push origin feature/sqrt

 
________________________________________
Step 5: Bug Fix in dev Branch (Divide Function)
Switch back:
git checkout dev
Fix divide function, then:
git add .
git commit -m "Fixed divide by zero bug"
git push origin dev
 
________________________________________
Step 6: Update Feature Branch with Latest Dev
git checkout feature/sqrt
git merge dev
(Resolve conflicts if any)
git push origin feature/sqrt
 
________________________________________
Step 7: Create Pull Request
On GitHub:
•	PR: feature/sqrt → dev
•	Request review from classmate
________________________________________
Step 8: Merge Feature into Dev
After approval:
git checkout dev
git merge feature/sqrt
git push origin dev

 
________________________________________
Step 9: Final Merge to Main (Version 2)
git checkout main
git merge dev
git push origin main
________________________________________
Q2: Git LFS (Large File Handling)
Step 1: Install Git LFS
git lfs install
 
________________________________________
Step 2: Create lfs Branch
git checkout -b lfs
 
________________________________________
Step 3: Track Large Files
Example for .zip:
git lfs track "*.zip"
 
________________________________________
Step 4: Add Large File (>200MB)
git add .gitattributes
git add your-large-file.zip
git commit -m "Added large file using Git LFS"
git push origin lfs
 
________________________________________
Step 5: Verify (Clone Repo)
git clone https://github.com/niteshkvlk/git_assignment_HeroVired.git
cd git_assignment_HeroVired
git checkout lfs
 
________________________________________
Q3: Geometry Calculator + Git Stash
Step 1: Create Branch
git checkout -b geometry-calculator
________________________________________
Step 2: Circle Feature
git checkout -b feature/circle-area
Make partial changes, then stash:
git stash
________________________________________
Step 3: Rectangle Feature
git checkout -b feature/rectangle-area
Make partial changes, then stash:
git stash
________________________________________
Step 4: Resume Circle Work
git checkout feature/circle-area
git stash pop
Complete code:
git add .
git commit -m "Completed circle area feature"
git push origin feature/circle-area

 
________________________________________
Step 5: Resume Rectangle Work
git checkout feature/rectangle-area
git stash pop
Complete code:
git add .
git commit -m "Completed rectangle area feature"
git push origin feature/rectangle-area
 
________________________________________
Step 6: Pull Requests
On GitHub:
•	PR: feature/circle-area → dev
•	PR: feature/rectangle-area → dev
________________________________________
Step 7: Merge After Review
git checkout dev
git merge feature/circle-area
git merge feature/rectangle-area
git push origin dev
 
________________________________________
Step 8: Final Merge to Main
git checkout main
git merge dev
git push origin main

 
 
________________________________________ Extra (Important for Marks)
Add Collaborator
GitHub → Settings → Collaborators → Add classmate
 
________________________________________
Review Classmate Code
•	Go to their repo → Pull Request → Add comments
________________________________________


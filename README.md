# Flexion Coding Development Branch

## Purpose
This branch is used for testing purposes and fulfills the following roles:

1. The branch 'development' is the developer's workspace. Any development that is to be made will be done on a branch and merged in

2. This branch continuously integrates and deploys code the the TEST server upon commit/push and code review by the development team 

3. Once this branch is in a stable state and ready for release, a pull request can be made to merge 'development' into 'master'.

4. Upon successful code review and merge into 'master', Jenkins will deploy the code to the PROD server
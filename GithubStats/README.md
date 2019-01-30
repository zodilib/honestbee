####Steps 

1. Clone the Repo
    ```
    git clone https://github.com/zodilib/honestbee.git
    ```
2.  Build the Image 
    ```
    docker build -t <image_name> .
    ```

3. Run the Container 
    ```
    docker run -v $PWD:/opt <image_name>  <list of repos>
    ```

4. This will create a new file "repoinfo.csv" 


####Example -
    ``` 
    #docker build -t repoinfo .
    #docker run -v $PWD:/opt repoinfo  example_list.txt
    ```





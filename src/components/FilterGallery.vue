<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          src="https://cdn.iconscout.com/icon/free/png-256/gallery-44-267592.png"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Gallery Filter
        </h1>

        <p class="subheading font-weight-regular">
          請上傳你要濾鏡的圖片
          <br>圖片格式限制jpg/png
        </p>
        <v-row class="text-center">
      <v-col cols="11">
         <v-file-input
          id="file"
          ref="upload"
          type="file"
          accept="image/png, image/jpeg, image/bmp"
          placeholder="Pick an image"
          prepend-icon="mdi-camera"
          label="圖片"
          @change="showImage"
        ></v-file-input>
      </v-col>
       <v-col cols="1">
         <v-btn
          :loading="loading3"
          :disabled="loading3"
          color="blue-grey"
          class="ma-2 white--text"
          @click="uploadFile()"
        >
          <v-icon
            right
            dark
          >
            mdi-cloud-upload
          </v-icon>
        </v-btn>
      </v-col>
      </v-row>
      
      </v-col>

    </v-row>
    <v-row dense>
        <v-col
          cols="6"
        >
          <v-card>
            <v-img
              :src="original"
              class="white--text align-end"
              height="400px"
            >
              <v-card-title >原始圖片</v-card-title>
            </v-img>
              <v-card-text>
                <v-container fluid>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="sigma"
                        max="50"
                        min="-50"
                        thumb-label="always"
                        label="SIGMA"
                      ></v-slider>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="phie"
                        max="50"
                        min="-50"
                        thumb-label="always"
                        label="PHIE"
                      ></v-slider>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-slider
                          v-model="tau"
                          max="50"
                          min="-50"
                          thumb-label="always"
                          label="TAU"
                        ></v-slider>
                    </v-col>
                </v-row>
                </v-container>
                </v-card-text>
          </v-card>
        </v-col>
        <v-col
          cols="6"
        >
          <v-card>
            <v-img
              :src="final"
              class="white--text align-end"
              height="500px"
            >
              <v-card-title >運算後圖片</v-card-title>
            </v-img>
              
          </v-card>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
const BASE_URL = 'http://localhost:8080';
export default {
    name: 'FilterGallery',

    data: () => ({
      original:'/images/Final1.jpg',
      final:'/images/Final1.jpg',
      sigma: 0,
      phie:0,
      tau:0,
      loading3: false,
    }),
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]

        setTimeout(() => (this[l] = false), 3000)

        this.loader = null
      },
    },
    methods:{
      showImage(file) {
        const formData = new FormData()
        formData.append('fileImage',file)
         axios.post(`http://127.0.0.1:3000/upload`,formData,{headers: {'Content-Type': 'multipart/form-data'}})
        .then(res =>{
          console.log(res)
        })
        .catch(err =>{
          window.console.log(err)
        })
      },
      uploadFile(){
        // const formData = new FormData()
        
        axios.get(`http://127.0.0.1:3000/`)
        .then(res =>{
          console.log(res)
        })
        .catch(err =>{
          window.console.log(err)
        })
      },
      uploadImage (formData) {
        const url = `${BASE_URL}/photos/upload`;
        return axios.post(url, formData)
        // get data
        .then(x => x.data)
        // add url field
        .then(x => x.map(img => Object.assign({},
            img, { url: `${BASE_URL}/images/${img.id}` })));

      }
      
      
    }
  }
</script>
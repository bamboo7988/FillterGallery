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
        <v-col cols="12">
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
                    <v-col
                    class='text-h5'>
                    數值調整
                    </v-col>
                  </v-row>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="sigmaBF"
                        step="10"
                        ticks="always"
                        tick-size="4"
                        label="Bilateral filter"
                        color="blue-grey"
                        track-color="grey"
                        thumb-label
                      ></v-slider>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                      <v-slider
                        v-model="phieqCQ"
                        step="10"
                        ticks="always"
                        tick-size="4"
                        label="Color quantization"
                        color="blue-grey"
                        track-color="grey"
                        thumb-label
                      ></v-slider>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-slider
                          v-model="sigmaDE"
                          step="10"
                          ticks="always"
                          tick-size="4"
                          label="Dog edge"
                          color="blue-grey"
                          track-color="grey"
                          thumb-label
                        ></v-slider>
                    </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn
                      block
                      x-large
                      :loading="loading"
                      :disabled="loading"
                      color="blue-grey"
                      class="ma-2 white--text text-h5"
                      @click="caculate"
                    >
                      運算
                      <v-icon
                        right
                        dark
                      >
                        mdi-cloud-upload
                      </v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                </v-container>
                </v-card-text>
          </v-card>
        </v-col>
        <v-col
          cols="6"
        >
          <v-card v-if="isShow">
            <v-img
              :src="final"
              class="white--text align-end"
              height="400px"
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
const BASE_URL = 'http://localhost:3000';
export default {
    name: 'FilterGallery',

    data: () => ({
      original:'/upload/filename.jpg',
      final:'/upload/final.jpg',
      sigmaBF: 0,
      phieqCQ:0,
      sigmaDE:0,
      loading: false,
      isShow: false,
    }),
    computed: {
      getImageUrl: function() {
        return + this.photo;
      }
    },
    methods:{
      showImage(file) {
        const formData = new FormData()
        formData.append('fileImage',file)
         axios.post(`http://127.0.0.1:3000/upload`,formData,{headers: {'Content-Type': 'multipart/form-data'}})
        .then(res =>{
          console.log(res)
          this.visible = false;
          this.$forceUpdate();
        })
        .catch(err =>{
          window.console.log(err)
        })
      },
      caculate() {
        console.log('caculate')
        this.loading = true
        axios.get(`${BASE_URL}/call/python`, {  params: { sigmaBF: this.sigmaBF, phieqCQ: this.phieqCQ, sigmaDE: this.sigmaDE} })
        .then(res =>{
          if(res.statusText==='OK'){
            this.loading = false
            this.isShow = true
            this.$forceUpdate();
          }
        })
        .catch(err =>{
          window.console.log(err)
        })
      }

    }
  }
</script>
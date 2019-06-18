<template>
  <div>
    <el-form class="input-form" ref="form" :model="form">
        <el-form-item label="タイトル">
            <el-input v-model="form.title" placeholder="タイトル"></el-input>
        </el-form-item>
        <el-form-item label="詳細">
            <el-input type="textarea" :rows="6" placeholder="詳細" v-model="form.detail">
            </el-input>
        </el-form-item>
        <el-form-item label="カテゴリ">
            <el-select v-model="form.category" placeholder="選択してください">
                <el-option :value=1 label="家事代行"></el-option>
                <el-option :value=2 label="育児代行"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="掲載開始日">
            <el-date-picker v-model="form.publish_start_at" type="date" placeholder="掲載開始日"></el-date-picker>
        </el-form-item>
        <!-- <el-form-item label="添付ファイル">
            <el-upload action="/api/media" :on-success="onFileUploadSuccess" :on-error="onFileUploadError" :on-remove="onFileRemove" :headers="sendHeaders" :show-file-list="true">
                <el-button type="default">アップロード</el-button>
            </el-upload>
        </el-form-item> -->

        <el-form-item>
            <el-button type="primary" @click="save">保存</el-button>
        </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import moment from 'moment'
  export default {
    data () {
      return {
        form: {
          title: "",
          // image: "",
          category: "",
          publish_start_at: null,
          detail: "",
          // uploadFiles: []
        }
      }
    },
    methods: {
      onFileUploadSuccess (response, file, fileList) {
          this.uploadFiles.push(response.uuid)
      },
      onFileRemove (file, fileList) {
          let index = this.uploadFiles.indexOf(file.response.uuid)
          this.uploadFiles.splice(index, 1)
      },
      onFileUploadError (error, file, fileList) {
          this.$error('ファイルアップロードに失敗しました')
      },
      // 保存
      save () {
        let self = this
        const config = {
          headers: { "content-type": "multipart/form-data" }
        }
        let formData = new FormData();
        for (let data in this.form) {
          formData.append(data, this.form[data]);
        }
        this.$axios['post']('article/', formData, config).then(response => {
            self.$message('保存が完了しました')
            self.loading = false
            // this.$parent.$emit('savedTransaction')
        }).catch(error => {
            if (error.response) {
                let e = error.response.data
                self.$message.error(e.message + ' [' + e.code + ']')
            }
        })
      }
    }
  }

</script>

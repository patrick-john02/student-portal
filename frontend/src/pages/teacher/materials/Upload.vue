<script lang="ts">
export const description = "Teacher upload learning materials page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Label } from "@/components/ui/label"
import {
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
  SelectValue,
} from "@/components/ui/select"

import { UploadCloud, FileText, BookOpen } from "lucide-vue-next"

const userRole = "Teacher"

// Form state
const materialTitle = ref("")
const materialDesc = ref("")
const subject = ref("")
const section = ref("")
const file = ref<File | null>(null)

function handleFileChange(e: Event) {
  const target = e.target as HTMLInputElement
  if (target.files?.length) {
    file.value = target.files[0]
  }
}
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/materials">Materials</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Upload</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Page Title -->
        <div>
          <h2 class="text-2xl font-bold tracking-tight">Upload Learning Material</h2>
          <p class="text-sm text-muted-foreground">
            Upload documents, lectures, modules, or learning worksheets.
          </p>
        </div>

        <!-- Upload Form -->
        <Card>
          <CardHeader>
            <CardTitle>Material Information</CardTitle>
            <CardDescription>
              Fill in the details and upload your learning material.
            </CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <!-- Title -->
            <div class="grid gap-2">
              <Label>Material Title</Label>
              <Input
                v-model="materialTitle"
                placeholder="Enter material title..."
              />
            </div>

            <!-- Subject & Section -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="grid gap-2">
                <Label>Subject</Label>
                <Select v-model="subject">
                  <SelectTrigger>
                    <SelectValue placeholder="Select subject" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="Math">Math</SelectItem>
                    <SelectItem value="English">English</SelectItem>
                    <SelectItem value="Science">Science</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div class="grid gap-2">
                <Label>Section</Label>
                <Select v-model="section">
                  <SelectTrigger>
                    <SelectValue placeholder="Select section" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                    <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                    <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>

            <!-- Description -->
            <div class="grid gap-2">
              <Label>Description</Label>
              <Textarea
                v-model="materialDesc"
                placeholder="Short description of the learning material..."
                class="min-h-28"
              />
            </div>

            <!-- File Upload -->
            <div class="grid gap-2">
              <Label>Upload File</Label>

              <label
                class="flex flex-col items-center justify-center gap-3 border border-dashed rounded-xl p-6 cursor-pointer hover:bg-muted/40 transition"
              >
                <UploadCloud class="h-10 w-10 text-muted-foreground" />
                <div class="text-center">
                  <p class="font-semibold">Click to upload</p>
                  <p class="text-sm text-muted-foreground">
                    PDF, DOCX, PPT, images, etc.
                  </p>
                </div>

                <Input
                  type="file"
                  class="hidden"
                  @change="handleFileChange"
                />
              </label>

              <div v-if="file" class="flex items-center gap-2 text-sm mt-2">
                <FileText class="h-4 w-4" />
                <span>{{ file.name }}</span>
              </div>
            </div>

            <!-- Actions -->
            <div class="flex justify-end gap-2 pt-4">
              <Button variant="outline">Cancel</Button>

              <Button class="gap-2">
                <BookOpen class="h-4 w-4" />
                Upload Material
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>

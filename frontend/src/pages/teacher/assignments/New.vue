<script lang="ts">
export const description = "Teacher create new assignment page"
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
import { Select, SelectTrigger, SelectContent, SelectItem, SelectValue } from "@/components/ui/select"

import { Calendar, FilePlus2 } from "lucide-vue-next"

const userRole = "Teacher"

// form state
const title = ref("")
const instructions = ref("")
const dueDate = ref("")
const subject = ref("")
const section = ref("")
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
              <BreadcrumbLink href="/teacher/assignments">Assignments</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>New</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Create Assignment</h2>
            <p class="text-sm text-muted-foreground">
              Add a new assignment and publish it to your students.
            </p>
          </div>
        </div>

        <!-- Assignment Form -->
        <Card>
          <CardHeader>
            <CardTitle>Assignment Details</CardTitle>
            <CardDescription>
              Fill out the form to create a new classroom assignment.
            </CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <!-- Title -->
            <div class="grid w-full gap-2">
              <Label>Assignment Title</Label>
              <Input v-model="title" placeholder="Enter assignment title..." />
            </div>

            <!-- Subject & Section -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="grid w-full gap-2">
                <Label>Subject</Label>
                <Select v-model="subject">
                  <SelectTrigger>
                    <SelectValue placeholder="Select Subject" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="Math">Math</SelectItem>
                    <SelectItem value="English">English</SelectItem>
                    <SelectItem value="Science">Science</SelectItem>
                    <SelectItem value="Filipino">Filipino</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div class="grid w-full gap-2">
                <Label>Section</Label>
                <Select v-model="section">
                  <SelectTrigger>
                    <SelectValue placeholder="Select Section" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                    <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                    <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>

            <!-- Due Date -->
            <div class="grid w-full gap-2">
              <Label>Due Date</Label>
              <div class="relative">
                <Input type="date" v-model="dueDate" class="pr-10" />
                <Calendar class="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
              </div>
            </div>

            <!-- Instructions -->
            <div class="grid w-full gap-2">
              <Label>Instructions</Label>
              <Textarea
                v-model="instructions"
                placeholder="Add assignment instructions..."
                class="min-h-32"
              />
            </div>

            <!-- Actions -->
            <div class="flex justify-end gap-2">
              <Button variant="outline">Cancel</Button>
              <Button class="gap-2">
                <FilePlus2 class="h-4 w-4" />
                Create Assignment
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
